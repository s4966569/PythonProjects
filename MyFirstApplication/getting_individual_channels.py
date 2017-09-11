from PIL import Image

img = Image.open("beau.jpg")
r, g, b = img.split()

r.show()