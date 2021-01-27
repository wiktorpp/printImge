from PIL import Image, ImageOps

path = "C:\\Users\\Małgosia\\Desktop\\foxcopy.png"

image = Image.open(path).convert()
image = image.rotate(90, expand=True)
image = ImageOps.flip(image)
bitmap = image.load()
size = [image.size[0], image.size[1]]

print("bitmap = ", end="")

out = []
for row in range(size[0]):
    out.append([])
    for col in range(size[1]):
        pixel = bitmap[row, col]
        out[row].append([pixel[0], pixel[1], pixel[2]])

print(out)