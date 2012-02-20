# coding: utf-8
import Image, ImageFont, ImageDraw
import sys, logging

fontfamily = "/usr/share/fonts/truetype/takao/TakaoExGothic.ttf"

"""
fontsize = fとすると

1文字の大きさ
  width:  f/2 * 7文字 = 
  height: f   * 7文字 = 

中心点は
  X = startX + (7/4 * f)
  Y = startY + (7/2 * f)

画像の中心点は、
  width/2
  height/2

"""


try:
    width  = int(sys.argv[1])
    height = int(sys.argv[2])
    fontsize = int(sys.argv[3])
    image  = Image.new("RGB", (width,height))
    draw   = ImageDraw.Draw(image)
    font   = ImageFont.truetype(fontfamily,fontsize)
    draw.text((32, 32), u"%dx%d" % (width,height), font=font)
    image.save('%dx%d.png' % (width,height), 'PNG')
except:
    logging.error(sys.exc_info())

