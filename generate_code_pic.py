"""Generate an image verificaion code"""

import string
import random
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os, sys

(x,y)=(180,80) #image size
txt = Image.new("RGBA",(x,y),(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)))
draw = ImageDraw.Draw(txt)
fnt = ImageFont.truetype('Symbola_hint.ttf', 40) # set font and size of the text

draw.text((20,20),random.choice(string.ascii_letters), font=fnt,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255),255))
draw.text((60,20),random.choice(string.ascii_letters), font=fnt,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255),255))
draw.text((100,20),random.choice(string.ascii_letters), font=fnt,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255),255))
draw.text((140,20),random.choice(string.ascii_letters), font=fnt,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255),255))

outfile = "code.jpg"
# out = Image.alpha_composite(img, txt) #to use this function, image mode must be RGBA
txt.show()
txt.save(outfile,"JPEG")
