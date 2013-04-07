from parse import *

def parse_sig_command(query):
    p = parse("sig til {unick} at han {arg}",query)
    if str(p) != "None":
        return p['unick'] + ": Du " + p['arg'].replace("han","du").replace("sig","dig")

    p = parse("sig til {unick} han {arg}",query)
    if str(p) != "None":
        return p['unick'] + ": Du " + p['arg'].replace("han","du").replace("sig","dig")

    p = parse("sig til {unick} at hun {arg}",query)
    if str(p) != "None":
        return p['unick'] + ": Du " + p['arg'].replace("hun","du").replace("sig","dig")

    p = parse("sig til {unick} hun {arg}",query)
    if str(p) != "None":
        return p['unick'] + ": Du " + p['arg'].replace("hun","du").replace("sig","dig")

    p = parse("sig til {unick} at {arg}",query)
    if str(p) != "None":
        return p['unick'] + ": " + p['arg']

    return "Brug: sig til <person> at han/hun <besked>"
