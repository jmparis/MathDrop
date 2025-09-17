# https://www.youtube.com/watch?v=AalmiaowRxY
import math
from PIL import Image

width  = 2480
height = 3508

C = width/2
R = width/2

echiquier = Image.new('RGB', (width, height), (255,255,0))

for x in range(width):
    for y in range(height):
        x0 = x-width/2+0.5
        y0 = y-height/2+0.5
        f  = R**2/(x0**2+y0**2+0.000000000001)
        x1 = x0*f
        y1 = y0*f
        cx = math.floor(x1/C)
        cy = math.floor(y1/C)
        color = ((cx+cy)%2)*255
        echiquier.putpixel((x,y),(color,color,color))
        
echiquier.show()