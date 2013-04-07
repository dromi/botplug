#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import getpass
import sleekxmpp

from optparse import OptionParser
from parse import *
from parse import compile
from sig_til import parse_sig_command
from cmd_help import *
from open_hours import *
from bot_plugins.hey import *

# Python versions before 3.0 do not use UTF-8 encoding by default.
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input

class Botplug(sleekxmpp.ClientXMPP):

    def __init__(self, password):
        self.room = "snak@conference.orn.li"
        self.nick = "botplug"
        self.mail  = "spam.kran@gmail.com"
        self.parsedict = self.create_parse_dict()

        sleekxmpp.ClientXMPP.__init__(self, self.mail, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler('message', self.message)        
        self.add_event_handler("groupchat_message", self.muc_message)
        #self.add_event_handler("muc::%s::got_online" % self.room,
        #                       self.muc_online)

    def start(self, event):
        self.get_roster()
        self.send_presence()
        self.plugin['xep_0045'].joinMUC(self.room,
                                        self.nick,
                                        # If a room password is needed, use:
                                        # password=the_room_password,
                                        wait=True)
        #self.send_message(mto=self.room,
        #                  mbody="Nissen er i huset!",
        #                  mtype='groupchat')
        
    def muc_message(self, msg):
        if msg['body'].startswith(self.nick+":"):
            query = msg['body'][len(self.nick)+2:].lower().decode('utf-8')
            print("got query: " + query)

            if str(self.parsedict['sig'].parse(query)) != "None":
                self.say(parse_sig_command(msg,query))

            elif str(self.parsedict['hej'].parse(query)) != "None":
                self.say(hey(msg,query))

            elif str(self.parsedict['sov'].parse(query)) != "None":
                if str(msg['from']).endswith("Dromi"):
                    print("closing")
                    self.say("Botten går i seng :-(")
                    self.disconnect(wait=True)
                    exit(0)
                else:
                    self.say("DU IKKE MIN RIGTIGE FAR!!!!!")

            elif str(self.parsedict['hjæ'].parse(query)) != "None":
                p = self.parsedict['hjæ'].parse(query)
                self.say(get_command_help(p['command']))

            elif str(self.parsedict['kom'].parse(query)) != "None":
                self.say(get_command_list())

            elif str(self.parsedict['clo'].parse(query)) != "None":
                self.say(opening_hours())

            else:
                self.say("Kommandoen er mig ikke bekendt. Brug "+self.nick+": kommandoer for oversigt.")

    def message(self, msg):
        if msg['type'] in ('normal', 'chat'):
            print("Got personal message: " + msg['body'])
            msg.reply("det godt du hej!").send()

    # Only usable if the bot should speak when someone joins
    #def muc_online(self, presence):


    def say(self, body):
        self.send_message(mto=self.room,
                          mbody=body,
                          mtype='groupchat')

    def create_parse_dict(self):
        parsedict = {}
        parsedict['hej'] = compile(u"hej")
        parsedict['sig'] = compile(u"sig {}")
        parsedict['kom'] = compile(u"kommandoer")
        parsedict['hjæ'] = compile(u"hjælp {command}")
        parsedict['sov'] = compile(u"gå i seng")
        parsedict['clo'] = compile(u"closing time")
        return parsedict


if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)

    opts, args = optp.parse_args()

    # Setup logging.
    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')

    password = getpass.getpass("Password: ")

    # Setup the MUCBot and register plugins.
    bot = Botplug(password)
    bot.register_plugin('xep_0030') # Service Discovery
    bot.register_plugin('xep_0045') # Multi-User Chat
    bot.register_plugin('xep_0199') # XMPP Ping

    # Connect to the XMPP server and start processing XMPP stanzas.
    if bot.connect():
        bot.process(block=False)
        print("Done")
    else:
        print("Unable to connect.")

    while(True):
        inp = raw_input()
        if inp == "exit":
            print("closing")
            # nisse.say("Nissen går i seng :-(")
            bot.disconnect(wait=True)
            break
        elif inp.startswith("say "):
            bot.say(inp[4:])
        else:
            print("unknown input")
