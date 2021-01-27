from PIL import Image, ImageOps

path = "C:\\Users\\Małgosia\\Desktop\\image.png"

image = Image.open(path).convert()
image = image.rotate(90, expand=True)
image = ImageOps.flip(image)
bitmap = image.load()

size = [image.size[0], image.size[1]]
data = "{0:04x}{1:04x}\n".format(size[0], size[1])

out = []
for row in range(size[0]):
    for col in range(size[1]):
        pixel = bitmap[row, col]
        data += "{0:02x}{1:02x}{2:02x}{3:02x}".format(pixel[0], pixel[1], pixel[2], 0x00)
    data += "\n"

print(data)