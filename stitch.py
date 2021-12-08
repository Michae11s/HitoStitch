from PIL import Image, ImageDraw
import math
import random
random.seed()

size=800
st_len=25
bkg_col=(255,255,255)
st_col=(0,0,0,0)

h_prob=.2
v_prob=.5

img = Image.new('RGB', (size,size), color=bkg_col)
pixels=img.load()

#draw row stitches
for y in range(0,int(size/st_len)):
    start=0
    if random.randrange(1000) > (h_prob*1000):
        start=1
    for x in range(0,size):
        if (int(x/st_len) % 2) == start:
            pixels[x,y*st_len]=st_col

#draw vertical stitches
for x in range(0,int(size/st_len)):
    start=0
    if random.randrange(1000) > (v_prob*1000):
        start=1
    for y in range(0,size):
        if (int(y/st_len) % 2) == start:
            pixels[x*st_len,y]=st_col

img.show()
img.save('canvas.png')
