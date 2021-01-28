import os
import sys
esc = chr(0x1B)

#from heart import data, translucencyMask
from fox import data, translucencyMask
#from pebble import data

size = [
    int(data[0:4], 16),
    int(data[4:8], 16)
]
data = data[8:]
try: translucencyMask
except:
    translucencyMask = []
    for i in range(size[0]):
        translucencyMask.append([])
        for j in range(size[1]):
            translucencyMask[i].append(False)

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
            visibilityOdd = not translucencyMask[row][col]
            #bitField = "{0:2b}".format(pixelOdd[3])
            #visibilityOdd = not bool(int(bitField[0]))
            #print(bitField)
            #letter = bool(int(bitField[1]))
            #try:
            #    pixelEven = getPixel(row + 1, col)
            #    bitField = "{0:8b}".format(pixelEven[3])
            #    visibilityEven = not bool(bitField[0])
            #except:
            #    translucentEven = True
            try: 
                pixelEven = getPixel(row + 1, col)
                visibilityEven = not translucencyMask[row + 1][col]
            except: 
                visibilityEven = False
            if visibilityOdd == True and visibilityEven == True:
                sys.stdout.write(
                    f"{esc}[38;2;{pixelOdd[0]};{pixelOdd[1]};{pixelOdd[2]}m"
                )
                sys.stdout.write(
                    f"{esc}[48;2;{pixelEven[0]};{pixelEven[1]};{pixelEven[2]}m"
                )
                sys.stdout.write("▀")
            if visibilityOdd == False and visibilityEven == False:
                sys.stdout.write(f"{esc}[0m ")
            if visibilityOdd == True and visibilityEven == False:
                sys.stdout.write(
                    f"{esc}[38;2;{pixelOdd[0]};{pixelOdd[1]};{pixelOdd[2]}m"
                )
                sys.stdout.write(f"{esc}[49m")
                sys.stdout.write("▀")
            if visibilityOdd == False and visibilityEven == True:
                # The colors are flipped
                sys.stdout.write(f"{esc}[49m")
                sys.stdout.write(
                    f"{esc}[38;2;{pixelEven[0]};{pixelEven[1]};{pixelEven[2]}m"
                )
                sys.stdout.write("▄")
            
        print(f"{esc}[0m")
