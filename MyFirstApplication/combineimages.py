from PIL import Image

beau = Image.open("beau.jpg")
beau1 = Image.open("yy2016.png")

#位置的宽高必须跟要粘贴的图片的宽高一致
area = (0, 0, 448, 177)
beau.paste(beau1, area)

beau.show()