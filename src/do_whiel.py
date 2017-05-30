def do_whiel(d0, wh1le):
    if not callable(d0):
        raise ValueError('d0 is no function!, D0 MUST BE A FUNCTION')
    if not callable(wh1le) or type(wh1le) != bool:
        raise ValueError('wh1le is no boolean or boolyfunc!, WH1LE MUST BE A BOOLEAN OR A BOOLYFUNC')
    while True:
        d0()
        if callable(wh1le) and wh1le():
            break
        else if type(wh1le) == bool && wh1le:
            break
