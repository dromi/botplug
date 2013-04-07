from parse import *

def parse_sig_command(msg,query):
    reply = ""

    if str(parse("sig til {unick} at han {arg}",query)) != "None":
        p = parse("sig til {unick} at han {arg}",query)
        reply = p['unick'] + ": Du " + p['arg']

    elif str(parse("sig til {unick} hun {arg}",query)) != "None":
        p = parse("sig til {unick} han {arg}",query)
        reply = p['unick'] + ": Du " + p['arg']

    elif str(parse("sig til {unick} hun {arg}",query)) != "None":
        p = parse("sig til {unick} at hun {arg}",query)
        reply = p['unick'] + ": Du " + p['arg']

    elif str(parse("sig til {unick} hun {arg}",query)) != "None":
        p = parse("sig til {unick} hun {arg}",query)
        reply = p['unick'] + ": Du " + p['arg']

    elif str(parse("sig til {unick} at {arg}",query)) != "None":
        p = parse("sig til {unick} at {arg}",query)
        reply = p['unick'] + ": " + p['arg']

    else: 
        reply = "Brug: sig til <person> at han/hun <besked>"

    return reply.replace("han","du").replace("sig","dig").replace("hun","du").replace("sin","din").replace("jeg",msg['mucnick'])
