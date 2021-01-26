from PIL import Image
import os
import sys
esc = chr(0x1B)

os.system("")
image = Image.open("C:\\Users\\Małgosia\\Desktop\\heart.bmp").convert().rotate(90, expand=True)
bitmap = image.load()
#print(image.size)
size = [image.size[0], image.size[1]]
#import pdb; pdb.set_trace()

print("heart = ", end="")

out = []
for row in range(size[0]):
    out.append([])
    for col in range(size[1]):
        pixel = bitmap[row, col]
        #print(pixel)
        out[row].append([pixel[0], pixel[1], pixel[2]])
        #print(bitmap[row][col])

print(out)

#for row in out:
#    for pixel in row:
#        for color in pixel:
#            sys.stdout.write(("000" + str(color))[-3:])
#    #print("")