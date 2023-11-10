
from PIL import Image, ImageDraw, ImageFilter
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')

im1 = Image.open(os.path.join(picdir, 'NULL_COLOUR.png'))
im2 = Image.open(os.path.join(picdir, 'icon0.png'))
im2 = im2.convert("RGBA")
datas = im2.getdata()

newData = []

for item in datas:
    if item[3] == 0:
        newData.append((255, 255, 255, 255))
    else:
        newData.append(item)

im2.putdata(newData)

back_im = im1.copy()
back_im.paste(im2.resize((256, 256)), (20, 200))
back_im.save(os.path.join(picdir, 'icon0_new.bmp'), quality=95)

"""
amountImages = 10

#We go through the number of images we have in the folder
for i in range(1,amountImages+1):

    #we establish the path of the images
    path = os.path.dirname(os.path.abspath(__file__))

    #We create the input and output names of the images
    if(i>=1 and i<10):
        amountZeros ="000"
    elif(i>=9 and i<100):
        amountZeros ="00"
    elif(i>=99 and i<1000) :
        amountZeros ="0"
    else:
        amountZeros=""

    name_in = "/out{}{}.PNG".format(amountZeros,i)
    name_out = "/out{}{}.bmp".format(amountZeros,i)
    print(name_in,"---",name_out)
    
    #we open the image in png
    file_in = path + name_in
    img = Image.open(file_in)

    #we save the image in png
    file_out = path + name_out
    img.save(file_out)

    print("Imagen {} ok".format(i))
"""
