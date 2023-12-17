from PIL import Image, ImageDraw, ImageFilter
import os
import time
from API_Handler import villager_bday, pp, fromJSONgetName, getThumbnail, api_key, getNumOfBdays

# This will get the directory path of img/
dir_img = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
# This will get the directory path of lib/
dir_lib = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

# This will list all the items in the img/ (AKA it will list all the files)
#listdir_img = os.listdir(dir_img)

# These are useful definitions
newIconSize = (250, 250)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)



# Here we will create a function to run the API_nookipedia_test.py
def runAPI(file_path):
    try:
        os.system(f'python3 {os.path.join(file_path)}')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.\r\n")

# This function call will run the python script, therefore, if we want for main, we can use this for all
runAPI('lib/API_nookipedia_test.py')



##########################################################################################################################################
##########################################################################################################################################
######
######      "need to do with this code" list:
######              - I need to save the files as black_[insert character name here].bmp
######              - I need to save the files as red_[insert character name here].bmp
######                      - That way I can read the images in with the main.py
######              - https://stackoverflow.com/questions/15312953/choose-a-file-starting-with-a-given-string
######                      - This is a good explanation on how to do this
######              
######              
######              - Maybe I should create a function or class that will do everything and that function will take the number
######                of different images (i.e. img_[passed arg (0,1)]_name.png)
######
##########################################################################################################################################
########################################################################################################################################## 



########################################################################################################
# TEMP USE, DELETE AFTER THIS MODULE HAS BEEN COMPLETED
# This is what is needed to run the actual API download


# Allow 3 seconds to download image(s)
time.sleep(3)


##########################################################################################################################################
##########################################################################################################################################
######
######     Actual functionality of this script begins here
######      - Need to open the in files, out files
######     
##########################################################################################################################################
########################################################################################################################################## 

# Sets icon_file's path to be opened
    # This will open the first file it sees with 'img_'
for item in os.listdir(dir_img):
    if item.startswith('img_'):
        icon_file_path = os.path.join(dir_img, item)
        break   
print(item)

# Sets the blank canvas file's path to be opened
empty_canvas_file = os.path.join(dir_img, 'NULL_COLOUR.png')

# Opens the the blank canvas as background
background = Image.open(empty_canvas_file)
icon_open1 = Image.open(icon_file_path)     # Opens a iteration for RED of icon from API
icon_open2 = Image.open(icon_file_path)     # Opens a iteration for BLK of icon from API

# Resize and convert the obj for RED to the correct dimensions
icon_RED = icon_open1.resize(newIconSize)
icon_RED = icon_RED.convert("RGBA")

# Resize and convert the obj for BLK to the correct dimensions
icon_BLK = icon_open2.resize(newIconSize)
icon_BLK = icon_BLK.convert("RGBA")

# This gets the RGBA data from the actual image and put its in the obj
img_red_data = icon_RED.getdata()
img_blk_data = icon_RED.getdata()


# This sets the outfile location, name and type
outFile_RED = os.path.join(dir_img, 'color_test_red.bmp')
outFile_BLK = os.path.join(dir_img, 'color_test_black.bmp')


# This will create a border around the image
def addBorder(data):
    newData = []                # Temp data storage to hold image obj
    prevAlphaVAL = 0            # Check previous opacity

    for item in data:
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
    R_Image.paste(icon_RED, (20, 230))
    R_Image.save(outFile_RED, quality=95)

# Print Black BMP
def printBlackBMP(data):
    newData = []
    
    for item in data:
        #if (item[0] < 100 and item[1] < 100 and item[2] < 100):
        #    newData.append(BLACK)
        #elif (item[0] < 128 and item[1] > 30 and item[2] > 30):
            newData.append(item)
        #else:
        #    newData.append(WHITE)

    icon_BLK.putdata(newData)

    B_Image = background.copy()
    B_Image.paste(icon_BLK, (20, 230))
    B_Image.save(outFile_BLK, quality=95)

b = printBlackBMP(rmTransparency(addBorder(img_blk_data)))
r = printRedBMP(rmTransparency(addBorder(img_red_data)))

# This will remove the first file it sees with 'img_'
for item in os.listdir(dir_img):
    if item.startswith('img_'):
        os.remove(os.path.join(dir_img, item))
        break
