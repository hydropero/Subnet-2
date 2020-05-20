import math

def cidrconvert(cidr):
    temp = ['0', '0', '0', '0', '0', '0', '0', '0']
    totalsubsizelist = []
    stringedsublist = []
    if 0 <= cidr:
        maximum = 256
        total = 0
        current = 0
        counter = 0
        sizeofdiv = 2
        for i in range(0, cidr):
            current = maximum / sizeofdiv
            total += current
            sizeofdiv *= 2
        totalsubsizelist.append(math.floor(total))





    if cidr >= 8:
        maximum = 256
        total = 0
        current = 0
        counter = 0
        sizeofdiv = 2
        for i in range(8, cidr):
            current = maximum / sizeofdiv
            total += current
            sizeofdiv *= 2
        totalsubsizelist.append(math.floor(total))


    if cidr >= 16:
        maximum = 256
        total = 0
        current = 0
        counter = 0
        sizeofdiv = 2
        for i in range(16, cidr):
            current = maximum / sizeofdiv
            total += current
            sizeofdiv *= 2

        totalsubsizelist.append(math.floor(total))


    if cidr >= 24:
        maximum = 256
        total = 0
        current = 0
        counter = 0
        sizeofdiv = 2
        for i in range(24, cidr):
            current = maximum / sizeofdiv
            total += current
            sizeofdiv *= 2
        totalsubsizelist.append(math.floor(total))
    for i in totalsubsizelist:
        i = str(i)
        stringedsublist.append(i)

    test = ".".join(stringedsublist)

    return test


def dec_convert(decimal):
    decimaldict = {
        0: 0,
        128: 1,
        192: 2,
        224: 3,
        240: 4,
        248: 5,
        252: 6,
        254: 7,
        255: 8
    }
    decimallist = decimal.split(".")
    CIDR_total = 0
    for i in decimallist:
        i = int(i)
        CIDR_total += decimaldict.get(i, "Error invalid entry was submitted")
    print(CIDR_total)








