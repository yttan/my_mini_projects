"""Add a number in the top right corner of a picture.
Color of the number is red.
code in Python3"""

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os, sys
for infile in sys.argv[1:]:
    fname,ftype = os.path.splitext(infile)
    number = 1
    try:
        img=Image.open(infile).convert("RGBA")
        print("image format",img.format)
        print("image size",img.size)
        print("image mode",img.mode)
        (x,y)=img.size
        txt = Image.new(img.mode,img.size,(255,255,255,0))
        draw = ImageDraw.Draw(txt)
        fnt = ImageFont.truetype('Symbola_hint.ttf', 30) # set font and size of the text
        draw.text((x-20,5),str(number), font=fnt,fill=(255,0,0,255)) # print number in the top right corner of the originial picture
        # top left is (0,0)
        #text color red
        outfile = fname + "new.jpg"
        out = Image.alpha_composite(img, txt) #to use this function, image mode must be RGBA
        out.show()
        out.save(outfile,"JPEG")
        number = number+1
    except IOError:
        print("can not open", infile)
