from PIL import Image, ImageOps

path = "C:\\Users\\Małgosia\\Desktop\\image.png"

image = Image.open(path).convert("RGB")
image = image.rotate(90, expand=True)
image = ImageOps.flip(image)
bitmap = image.load()

size = [image.size[0], image.size[1]]
data = ""

print('translucencyMaskStr = """')

for row in range(size[0]):
    for col in range(size[1]):
        pixel = bitmap[row, col]
        if pixel == (255, 255, 255):
            data += "1"
        else:
            data += "0"
    data += "\n"

print(data)
print('"""[1:-1].splitlines()')