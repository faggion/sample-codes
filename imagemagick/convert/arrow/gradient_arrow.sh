#!/bin/sh

GRN='green'
convert -size 100x100 xc:#eeeeee -tile gradient:#ff0000-#ffffff -draw 'polygon 10,40 60,40 60,25 90,50 60,75 60,60 10,60' grad_arrow.png