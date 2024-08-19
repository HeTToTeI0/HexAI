import sys
clr = sys.argv[1]
def hextorgb(hexz):
    return tuple(int(hexz[i:i+2], 16) for i in (0, 2, 4))

print(hextorgb(clr))
