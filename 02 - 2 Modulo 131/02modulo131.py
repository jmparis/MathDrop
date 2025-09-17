# https://www.youtube.com/watch?v=nwmuSzFXd8M
import math
from PIL import Image, ImageDraw

width  = 1240
height = 1240
cx = width/2
cy = height/2
R  = 580
N  = 131
table = 2

multi = Image.new('RGB', (width,height), (255,255,255))
draw  = ImageDraw.Draw(multi)
draw.ellipse((cx-R,cy-R,cx+R,cy+R), outline=(0,0,0), width=3)

for i in range(N):
    alpha = 2*math.pi*i/N
    draw.line((cx+R*math.sin(alpha),cy-R*math.cos(alpha),cx+R*math.sin(table*alpha),cy-R*math.cos(table*alpha)), fill=(0,0,0), width=2)

multi.show()
