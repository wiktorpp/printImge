import os
import sys
esc = chr(0x1B)

#from heart import data, transparencyMask
#from fox import data, transparencyMask
#from pebble import data

from test import data, transparencyMask

size = [
    int(data[0:4], 16),
    int(data[4:8], 16)
]
data = data[8:]
try: transparencyMask
except:
    transparencyMask = []
    for i in range(size[0]):
        transparencyMask.append([])
        for j in range(size[1]):
            transparencyMask[i].append(False)

def getPixel(x, y):
    offset = (x * size[1] + y) * 8
    return ([
        int(data[offset:offset + 2], 16),
        int(data[offset + 2:offset + 4], 16),
        int(data[offset + 4:offset + 6], 16),
        int(data[offset + 6:offset + 8], 16)
    ])

defaultBgState = True
pixelLastOdd = None
pixelLastEven = None
for row in range(0, size[0], 2):
    for col in range(size[1]):
        pixelOdd = getPixel(row, col)
        visibilityOdd = not transparencyMask[row][col]
        #bitField = "{0:2b}".format(pixelOdd[3])
        #visibilityOdd = not bool(int(bitField[0]))
        #print(bitField)
        #letter = bool(int(bitField[1]))
        #try:
        #    pixelEven = getPixel(row + 1, col)
        #    bitField = "{0:8b}".format(pixelEven[3])
        #    visibilityEven = not bool(bitField[0])
        #except:
        #    transparentEven = True
        try: 
            pixelEven = getPixel(row + 1, col)
            visibilityEven = not transparencyMask[row + 1][col]
        except: 
            visibilityEven = False

        if visibilityOdd == True and visibilityEven == True:
            sys.stdout.write(
                f"{esc}[38;2;{pixelOdd[0]};{pixelOdd[1]};{pixelOdd[2]}m"
            )
            sys.stdout.write(
                f"{esc}[48;2;{pixelEven[0]};{pixelEven[1]};{pixelEven[2]}m"
            )
            defaultBgState = False
            sys.stdout.write("▀")

        if visibilityOdd == False and visibilityEven == False:
            if defaultBgState == False:
                sys.stdout.write(f"{esc}[49m ")
                defaultBgState == True
            else:
                sys.stdout.write(" ")

        if visibilityOdd == True and visibilityEven == False:
            if not pixelOdd == pixelLastOdd:
                sys.stdout.write(
                    f"{esc}[38;2;{pixelOdd[0]};{pixelOdd[1]};{pixelOdd[2]}m"
                )
            if defaultBgState == False:
                sys.stdout.write(f"{esc}[49m")
                defaultBgState == True
            sys.stdout.write("▀")

        if visibilityOdd == False and visibilityEven == True:
            # The colors are flipped
            if defaultBgState == False:
                sys.stdout.write(f"{esc}[49m")
                defaultBgState == True
            sys.stdout.write(
                f"{esc}[38;2;{pixelEven[0]};{pixelEven[1]};{pixelEven[2]}m"
            )
            sys.stdout.write("▄")
        
        pixelLastOdd = pixelOdd
        pixelLastEven = pixelEven

    print(f"{esc}[0m")
