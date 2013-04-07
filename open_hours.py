#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import datetime
import re

now = datetime.datetime.now()
weekday = now.weekday()

huse = ["http://www.magasin.dk/Kgs.-Nytorv/kongensnytorv,default,pg.html",
        "http://www.magasin.dk/Lyngby/lyngby,default,pg.html",
        "http://www.magasin.dk/Field%27s/fields,default,pg.html",
        "http://www.magasin.dk/R%C3%B8dovre/roedovre,default,pg.html",
        "http://www.magasin.dk/Odense/odense,default,pg.html",
        "http://www.magasin.dk/%C3%85rhus/aarhus,default,pg.html"]

section_re = "(?s)<div class=\"openinghours\">.*?</li>"
line_re = "<div class=\"ohhours\".*</div>"

def opening_hours():

    hours = []
    msg = ""

    for h in huse:
        site = urllib2.urlopen(h).read()
        tables = re.findall(section_re,site)
        lines = re.findall(line_re,tables[0])
        lines.pop(5)
        hours.append(re.split("<|>",lines[weekday])[2])
        
    msg += "\nMagasin åbningstider for " + now.strftime('%A %d. %B - %G') + "\n\n"
    msg += "Kongens Nytorv \t\t" + hours[0] + "\n"
    msg += "Lyngby \t\t\t\t" + hours[1] + "\n"
    msg += "Fields \t\t\t\t" + hours[2] + "\n"
    msg += "Rødovre \t\t\t\t" + hours[3] + "\n"
    msg += "Odense \t\t\t\t" + hours[4] + "\n"
    msg += "Århus \t\t\t\t" + hours[5]

    return msg
