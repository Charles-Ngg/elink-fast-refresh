#!/usr/bin/python
# -*- coding:utf-8 -*-
import epdconfig
import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd2in7.EPD()
    epd.init()
    epd.Clear(0xFF)
    
    # Drawing on the Horizontal image

    # Drawing on the Vertical image
   # Limage = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)  # 255: clear the frame

    
    font24 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 24)

    while 1:
       # t1=time.time()
        Himage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 255: clear the frame
        #t2=time.time()
        #print("1:"+str(t2-t1))

        draw = ImageDraw.Draw(Himage)
        #t3=time.time()
        #print("2:"+str(t3-t2))
        draw.text((10, 0), 'hello world', font = font24, fill = 0)
        draw.text((10,30),str(time.time()),font =font24 ,fill=0)
        #t4=time.time()
       # print("3:"+str(t4-t3))
        epd.display(epd.getbuffer(Himage))
        #t5=time.time()
       # print("4:"+str(t5-t4))
        epdconfig.delay_ms(100)
        print(str(time.time()))
        



except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()

