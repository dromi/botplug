#!/usr/bin/env python
# -*- coding: utf-8 -*-

hdict = {}
hdict[u'hej']  = "Hils på den flinke bot"
hdict[u'hjælp'] = "Få hjælp til bottens kommandoer"
hdict[u'sig'] = "Brug botten som en væmmelig midtermand\nSyntax: sig til <person> at han/hun <besked>"
hdict[u'kommandoer'] = "Få botten til at liste mulige kommandoer. Bemærk, det kun er første ord af hver kommando der gives."
hdict[u'gå'] = "Bed botten gå i seng\nSyntax: gå i seng"
hdict[u'closing'] = "Få oplyst dagens åbningstider for Magasin\nSyntax: closing time"

def get_command_list():
    msg = "Jeg har følgende kommandoer:\n"
    for k in hdict.keys()[:-1]:
        msg += k + ", "
    msg += hdict.keys()[-1]
    return msg

def get_command_help(command):
    if command in hdict:
        return command + ":\n" + hdict[command]
    else:
        return "Ukendt kommando. Der kan kun gives hjælp til gyldige kommandoer"
