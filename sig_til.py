from parse import parse


def parse_sig_command(msg, query):
    reply = ""

    if str(parse("sig til {unick} at {arg}", query)) != "None":
        p = parse("sig til {unick} at {arg}", query)
        reply = p['unick'] + ": " + p['arg']

    else: 
        reply = "Brug: sig til <person> at <besked>"

    replace_dict = (
        ('jeg', msg['mucnick']),
        ('du', 'jeg'),
        ('han', 'du'),
        ('hun', 'du'),
        ('sig', 'dig'),
        ('min', msg['mucnik']),
        ('din', 'min'),
        ('sin', 'din'),
        ('dit', 'mit'),
        ('dine', 'mine'),
        ('sine', 'dine'),
        ('ham', 'dig'),
        ('hende', 'dig'),
    )

    for old, new in replace_dict:
        reply = reply.replace(old, new)

    return reply
