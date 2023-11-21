
from PIL import Image, ImageDraw, ImageFilter
import os

############################################################################################################################################################
############################################################################################################################################################
######
######                  "Things to note" list:
######                      - This does not work at the moment, only with given file names
######
######
############################################################################################################################################################
############################################################################################################################################################


picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')

icon_file = os.path.join(picdir, 'icon0.png')
empty_canvas_file = os.path.join(picdir, 'NULL_COLOUR.png')

outFile_RED = os.path.join(picdir, 'color_test_red.bmp')
outFile_BLACK = os.path.join(picdir, 'color_test_black.bmp')

newIconSize = (300, 300)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
#TRANSPARENT = (x, y, z, 0)

background = Image.open(empty_canvas_file)
icon_open1 = Image.open(icon_file)
icon_open2 = Image.open(icon_file)

icon_RED = icon_open1.resize(newIconSize)
icon_RED = icon_RED.convert("RGBA")

icon_BLACK = icon_open2.resize(newIconSize)
icon_BLACK = icon_BLACK.convert("RGBA")

#newData = icon_RED.getdata()
datas = icon_RED.getdata()


# This will create a border around the image
def addBorder(data):
    newData = []
    prevAlphaVAL = 0

    for item in datas:
        if(prevAlphaVAL != item[3]):
            newData.append(BLACK)
        else:
            newData.append(item)
        prevAlphaVAL = item[3]
    return newData


# This will removed the transparency and replace it with a solid white
def rmTransparency(data):
    newData = []
    for item in data:
        if item[3] == 0:
            newData.append((255, 255, 255, 255))
        else:
            newData.append(item)
    return newData
# Print Red BMP
def printRedBMP(data):
    newData = []
    
    for item in data:
        if (item[0] > 128 and item[1] < 128 and item[2] < 128):
            # If red is the heaviest color, we want that to be a pixel
            newData.append(item)
        else:
            # Append white pixel if there is little red
            newData.append(WHITE)

    icon_RED.putdata(newData)

    R_Image = background.copy()
    R_Image.paste(icon_RED, (20, 200))
    R_Image.save(outFile_RED, quality=95)

# Print Black BMP
def printBlackBMP(data):
    newData = []
    
    for item in data:
        if (item[0] < 100 and item[1] < 100 and item[2] < 100):
            newData.append(BLACK)
        elif (item[0] < 128 and item[1] > 30 and item[2] > 30):
            newData.append(item)
        else:
            newData.append(WHITE)

    icon_BLACK.putdata(newData)

    B_Image = background.copy()
    B_Image.paste(icon_BLACK, (20, 200))
    B_Image.save(outFile_BLACK, quality=95)

r = printRedBMP(rmTransparency(addBorder(datas)))
b = printBlackBMP(rmTransparency(addBorder(datas)))