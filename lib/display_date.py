#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
#libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
#if os.path.exists(libdir):
#    sys.path.append(libdir)

import logging
import initEPD7in5 as epd7in5b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

import API_nookipedia as nookAPI

import datetime

date = datetime.datetime.now()

logging.basicConfig(level=logging.DEBUG)

##########################################################################################################################################
##########################################################################################################################################
######
######      "need to do with this code" list:
######              - This will be my main.py
######              - I will call the color_test.py to convert x-number of .png files to be converted, the file_n_color_convert.py
######                should purely change the files to:
######                           red_[char name].bmp
######                         black_[char name].bmp
######              - 
######              - 
######              - 
##########################################################################################################################################
########################################################################################################################################## 




try:
    logging.info("epd7in5b_V2 Demo")

    epd = epd7in5b_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font48 = ImageFont.truetype(os.path.join(fontdir, 'FinkHeavy.ttf'), 48)
    font72 = ImageFont.truetype(os.path.join(fontdir, 'FinkHeavy.ttf'), 72)
    """
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    Other = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Himage)
    draw_other = ImageDraw.Draw(Other)
    draw_Himage.text((10, 0), 'hello world', font = font24, fill = 0)
    draw_Himage.text((10, 20), '7.5inch e-Paper', font = font24, fill = 0)
    draw_Himage.text((150, 0), u'微雪电子', font = font24, fill = 0)    
    draw_other.line((20, 50, 70, 100), fill = 0)
    draw_other.line((70, 50, 20, 100), fill = 0)
    draw_other.rectangle((20, 50, 70, 100), outline = 0)
    draw_other.line((165, 50, 165, 100), fill = 0)
    draw_Himage.line((140, 75, 190, 75), fill = 0)
    draw_Himage.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw_Himage.rectangle((80, 50, 130, 100), fill = 0)
    draw_Himage.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage),epd.getbuffer(Other))
    time.sleep(2)

    # Drawing on the Vertical image
    logging.info("2.Drawing on the Vertical image...")
    Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    Limage_Other = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Limage)
    draw_Himage_Other = ImageDraw.Draw(Limage_Other)
    draw_Himage.text((2, 0), 'hello world', font = font18, fill = 0)
    draw_Himage.text((2, 20), '7.5inch epd', font = font18, fill = 0)
    draw_Himage_Other.text((20, 50), u'微雪电子', font = font18, fill = 0)
    draw_Himage_Other.line((10, 90, 60, 140), fill = 0)
    draw_Himage_Other.line((60, 90, 10, 140), fill = 0)
    draw_Himage_Other.rectangle((10, 90, 60, 140), outline = 0)
    draw_Himage_Other.line((95, 90, 95, 140), fill = 0)
    draw_Himage.line((70, 115, 120, 115), fill = 0)
    draw_Himage.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw_Himage.rectangle((10, 150, 60, 200), fill = 0)
    draw_Himage.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Limage), epd.getbuffer(Limage_Other))
    time.sleep(2)
    """
    logging.info("3. Reading Custom BMP files")

# This will display the day, month and date of any day of the year

    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    Other = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Himage)
    draw_other = ImageDraw.Draw(Other)

        # Month Date
    draw_Himage.text((10, 90), date.strftime("%B %-d"), font = font48, fill = 0)
        # Day of the week
    draw_other.text((10, 10), date.strftime("%A"), font = font72, fill = 0)

    epd.display(epd.getbuffer(Himage),epd.getbuffer(Other))
    time.sleep(5)



    """
    with Image.open(os.path.join(picdir, 'jan2.bmp')).convert("RGBA") as base:

        text = Image.new("RGBA", base.size, (255,255,255,0))
        newImage = ImageDraw.Draw(text)

        newImage.text((10,10), "Hello World", font=font32, fill=(255,255,255,255))

        out = Image.alpha_composite(base, text)

#    Himage = Image.open('halloween_bl.bmp')
    #Himage = Image.open(os.path.join(picdir, 'jan2.bmp'))
#    Himage_Other = Image.open(os.path.join(picdir, '7in5_V2_r.bmp'))
    Himage_Other = Image.open(os.path.join(picdir, 'NULL_COLOUR.bmp'))
    epd.display(epd.getbuffer(Himage), epd.getbuffer(Himage_Other))
    time.sleep(5)
 
    logging.info("4.read bmp file on window")
    Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    Himage2_Other = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '2in9.bmp'))
    Himage2.paste(bmp, (50,10))
    Himage2_Other.paste(bmp, (50,300))
    epd.display(epd.getbuffer(Himage2), epd.getbuffer(Himage2_Other))
    time.sleep(2)
    """
#    logging.info("Clear...")
#    epd.init()
#    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()
