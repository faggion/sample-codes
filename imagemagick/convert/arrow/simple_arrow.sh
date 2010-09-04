#!/bin/sh

GRN='green'
convert -size 100x100 xc:white -fill $GRN -draw 'rectangle 10,40 70,60' -draw 'polygon 60,25 60,75 90,50' simple_arrow.png