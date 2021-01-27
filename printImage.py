import os
import sys
esc = chr(0x1B)

data = """
000a000b
ffffff00ffffff000000000000000000ffffff00ffffff00ffffff000000000000000000ffffff00ffffff00
ffffff0000000000e0204000e020400000000000ffffff0000000000e0204000e020400000000000ffffff00
00000000e0204000ffffff00ffffff00e020400000000000e0204000e0204000e0204000e020400000000000
00000000e0204000ffffff00e0204000e0204000e0204000e0204000e0204000e0204000e020400000000000
00000000e0204000e0204000e0204000e0204000e0204000e0204000e0204000e0204000e020400000000000
ffffff0000000000e0204000e0204000e0204000e0204000e0204000e0204000e020400000000000ffffff00
ffffff00ffffff0000000000e0204000e0204000e0204000e0204000e020400000000000ffffff00ffffff00
ffffff00ffffff00ffffff0000000000e0204000e0204000e020400000000000ffffff00ffffff00ffffff00
ffffff00ffffff00ffffff00ffffff0000000000e020400000000000ffffff00ffffff00ffffff00ffffff00
ffffff00ffffff00ffffff00ffffff00ffffff0000000000ffffff00ffffff00ffffff00ffffff00ffffff00
""".replace('\n','')
#print(data)
size = [
    int(data[0:4], 16),
    int(data[4:8], 16)
]
data = data[8:]

def getPixel(x, y):
    offset = (x * size[1] + y) * 8
    return ([
        int(data[offset:offset + 2], 16),
        int(data[offset + 2:offset + 4], 16),
        int(data[offset + 4:offset + 6], 16),
        int(data[offset + 6:offset + 8], 16)
    ])

for row in range(size[0]):
    if row%2 != 0:
        continue
    else:
        for col in range(size[1]):
            pixelOdd = getPixel(row, col)
            sys.stdout.write(
                f"{esc}[38;2;{pixelOdd[0]};{pixelOdd[1]};{pixelOdd[2]}m"
            )
            try:
                pixelEven = getPixel(row + 1, col)
                sys.stdout.write(
                    f"{esc}[48;2;{pixelEven[0]};{pixelEven[1]};{pixelEven[2]}m"
                )
            except:
                sys.stdout.write(f"{esc}[49m")
            sys.stdout.write("▀")
        print(f"{esc}[0m")
