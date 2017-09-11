from PIL import Image

img = Image.open("beau.jpg")
area = (200, 300, 500, 600)
cropped_img = img.crop(area)
img.show()
cropped_img.show()