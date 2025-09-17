# https://www.youtube.com/watch?v=BCR7IhRFNDo
import math
from PIL import Image, ImageDraw

width  = 1748
height = 1240

pytha = Image.new("RGB", (width, height), (255, 255, 255))
draw  = ImageDraw.Draw(pytha, 'RGBA')

L = 200
alpha = math.pi/180*22.5
A0 = (width/2-L/2+300,1000)
B0 = (width/2+L/2+300,1000)

def arbre(A,B,n):
    C = sim(B,A,-math.pi/2,1)
    D = sim(A,B, math.pi/2,1)   
    draw.polygon([A,B,C,D],fill=(0,0,0,125),outline=(50,50,50,255))
    if (n>0) and (length(A,B)>1):
        E = sim(D,C,alpha,math.cos(alpha))
        arbre(D,E,n-1)
        arbre(E,C,n-1)

# Similitude
def sim(A,B,alpha,mu):
    C = [B[0]-A[0],B[1]-A[1]]
    D = [mu*(C[0]*math.cos(alpha) + C[1]*math.sin(alpha)),mu*(-C[0]*math.sin(alpha) + C[1]*math.cos(alpha))]
    return (A[0]+D[0],A[1]+D[1])

def length(A,B):
    return math.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)

arbre(A0,B0,200)

pytha.show()
