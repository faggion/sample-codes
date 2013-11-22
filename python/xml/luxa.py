# coding: utf-8
from xml.etree.ElementTree import *

tree = parse("/tmp/luxa.xml")
elem = tree.getroot()

for i in elem.findall(".//item"):
    #if i.find("./category_cd").text == 'BTY':
    img = i.find("./shop_img_1").text
    url = i.find("./url").text
    print '<a href="%s" target="_blank"><img src="%s"></a>' % (url, img)
