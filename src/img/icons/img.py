from PIL import Image

image = Image.open('logo-color.png')
print(f"Original size : {image.size}") #

image.resize((72,72)).save('apple-icon-72x72.png')
image.resize((57,57)).save('apple-touch-icon-57x57.png')
image.resize((60,60)).save('apple-touch-icon-60x60.png')
image.resize((114,114)).save('apple-touch-icon-114x114.png')
image.resize((120,120)).save('apple-touch-icon-120x120.png')
image.resize((144,144)).save('apple-touch-icon-144x144.png')
image.resize((152,152)).save('apple-touch-icon-152x152.png')
image.resize((16,16)).save('favicon-16x16.png')
image.resize((32,32)).save('favicon-32x32.png')
image.resize((64,64)).save('favicon-64x64.png')
image.resize((310,310)).save('largetile.png')
image.resize((150,150)).save('mediumtile.png')
image.resize((70,70)).save('smalltile.png')
image.resize((311,150)).save('widetile.png')



# sunset_resized = image.resize((400, 400))
# sunset_resized.save('sunset_400.jpeg')
