from PIL import Image, ImageFilter

img = Image.open('C:/Users/Adrian/Desktop/Python ZTM V2/section 17/pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
# filtered_img.save("grey.png", 'png')
# filtered_img.show()
# crooked = filtered_img.rotate(90).save("grey.png", 'png')
resize = filtered_img.resize((300, 300))
resize.save("grey.png", 'png')
print(img.size)