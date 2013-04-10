from parse import parse


def parse_sig_command(msg, query):
    reply = ""

    if str(parse("sig til {unick} at {arg}", query)) != "None":
        p = parse("sig til {unick} at {arg}", query)
        reply = p['unick'] + ": " + p['arg']

    else:
        reply = "Brug: sig til <person> at han/hun <besked>"

    replace_dict = {
        "han": "du",
        "hun": "du",
        "sig": "dig",
        "din": "min",
        "sin": "din",
        "dit": "mit",
        "jeg": msg['mucnick'],
    }

    for old, new in replace_dict.items():
        reply = reply.replace(old, new)

    return reply
