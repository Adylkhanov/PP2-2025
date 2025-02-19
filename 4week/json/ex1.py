import json

with open('sample-data.json') as f:
    main = json.load(f)
    print('''
    Interface Status
    ================================================================================
    DN                                                 Description           Speed    MTU  
    -------------------------------------------------- --------------------  ------  ------
    ''')
    data = main['imdata']
    for item in data:
        item = item['l1PhysIf']
        atrib = item['attributes']
        dn = atrib['dn']
        speed = atrib['speed']
        mtu = atrib['mtu']
        out = ''
        if len(dn) == 42:
            out += dn + '                              ' + speed + '   ' + mtu
        else:
            out += dn + '                              ' + speed + '   ' + mtu
        print(out)