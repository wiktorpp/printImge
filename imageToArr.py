from PIL import Image

path = "C:\\Users\\Małgosia\\Desktop\\heart.bmp"

image = Image.open(path).convert().rotate(90, expand=True)
bitmap = image.load()
size = [image.size[0], image.size[1]]

print("bitmap = ", end="")

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