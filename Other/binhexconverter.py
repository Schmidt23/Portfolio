"""Ohne Vorzeichen: base10 --> hexa + binary
Mit Vorzeichen(klein) in bin oder hexa
Hexabuchstaben sind Caps!"""

num = raw_input("N?  ")
##############################################################################
total = []
hx = []

def binary(num):
    for i in xrange(len(num)):
        k = (int(num[i]) * 2 ** (len(num) -i - 1))
        total.append(k)


def hexa(num):
    con = dict(A=10, B=11, C=12, D=13, E=14, F=15)

    for i in num:
        for k, v in con.items():
            if k == i:
                i = v
        hx.append(i)

    for i in xrange(len(hx)):
        k = (int(hx[i]) * 16 ** (len(hx) - i - 1))
        total.append(k)

##############################################################################

bits = []
its = []
n = 0

def to_bin(no):
    no = int(no)
    for i in its:
        if no - 2**i >= 0:
            bits.append("1")
            no = no-2**i
        else:
            bits.append("0")
###############################################################################

x = 0
nibs = []
dibs = []
hexas = []

def to_hex(no):
    no = int(no)
    con = dict(A=10, B=11, C=12, D=13, E=14, F=15)
    for i in nibs:
        if no - 16**i >= 0:
            add = no/16**i
            if add >= 16:
                dibs.append(15)
                no = no - 16**i * 15
            else:
                dibs.append("%s" %add)
                no = no-16**i*add
        else:
            dibs.append("0")
    for i in dibs:
        for k,v in con.items():
            if str(v) == i:
                i = str(k)
        hexas.append(i)

###############################################################################


if num[0] == "b":
    num = num[1::]
    binary(num)
    print sum(total)
elif num[0] == "h":
    num = num[1::]
    hexa(num)
    print sum(total)
else:
    while 2 ** n <= int(num):
        n += 1
    for i in xrange(0, n):
        its.append(i)
    its = sorted(its, reverse=True)
    to_bin(num)
    print "Binary: " + "".join(bits)
    while 16 ** x <= int(num):
        x += 1
    for i in xrange(0, x):
        nibs.append(i)
    nibs = sorted(nibs, reverse=True)
    to_hex(num)
    print "HExadecimal: " + "".join(hexas)

