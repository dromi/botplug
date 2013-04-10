from parse import parse

def parse_sig_command(msg,query):
    reply = ""

    if str(parse("sig til {unick} at {arg}",query)) != "None":
        p = parse("sig til {unick} at {arg}",query)
        reply = p['unick'] + ": " + p['arg']

    else: 
        reply = "Brug: sig til <person> at han/hun <besked>"

    reply = reply.replace("han","du")
    reply = reply.replace("hun","du")
    reply = reply.replace("sig","dig")
    reply = reply.replace("din","min")
    reply = reply.replace("sin","din")
    reply = reply.replace("dit","mit")
    reply = reply.replace("jeg",msg['mucnick'])
    
    return reply
