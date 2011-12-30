# coding: utf-8
import Image, ImageFont, ImageDraw

image = Image.new("RGB", (200,100))
draw  = ImageDraw.Draw(image)

# use a truetype font
font = ImageFont.truetype("/usr/share/fonts/truetype/takao/TakaoExGothic.ttf", 32)

draw.text((20, 32), u"あいうえお", font=font)

image.save('foo.png', 'PNG')
