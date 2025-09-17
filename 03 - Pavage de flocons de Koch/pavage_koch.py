# https://www.youtube.com/watch?v=vBh-S9u4utY
import math
from PIL import Image, ImageDraw

width  = 1748
height = 1240

vonkoch = Image.new('RGB', (width,height), (255,255,255))
draw = ImageDraw.Draw(vonkoch)

def koch(A,B,n):
    if (n==0):
        draw.line((A,B), fill=(0,0,0), width=1)
    else:
        M2 = sim(A,B,math.pi/6,1/math.sqrt(3))
        koch(M2,A,n-1)
        koch(B,M2,n-1)

def sim(A,B,alpha,mu):
    C = [B[0]-A[0],B[1]-A[1]]
    D = [mu*(C[0]*math.cos(alpha)+C[1]*math.sin(alpha)),mu*(-C[0]*math.sin(alpha)+C[1]*math.cos(alpha))]
    return [A[0]+D[0],A[1]+D[1]]
    
def flocon(A,B):
    C = sim(B,A,math.pi/3,1)
    koch(A,B,14)
    koch(B,C,14)
    koch(C,A,14)

L = 600
for i in range(3):
    for j in range(3):
        A0 = [1748/2+L/2+L*(i-1),height/2+L*math.sqrt(3)/6+L*2/3*math.sqrt(3)*(j-1)+L/3*math.sqrt(3)*(i-1)]
        B0 = [1748/2-L/2+L*(i-1),height/2+L*math.sqrt(3)/6+L*2/3*math.sqrt(3)*(j-1)+L/3*math.sqrt(3)*(i-1)]
        flocon(A0,B0)

vonkoch.show()