import math
import random
from PIL import Image, ImageDraw

width  = 1000
height = 1000

image = Image.new("RGB", (width, height), "black")
draw  = ImageDraw.Draw(image)

cote = 20
N = 2

dominos = [
    [0, 1, 0, 0],
    [2, 1, 0, 2],
    [0, 2, 2, 0],
    [0, 0, 0, 0]
]

def traceDominos():
    for i in range(2*N):
        for j in range(2*N):
            if (dominos[i][j]==1):
                draw.rectangle(
                    (
                        width/2+(j-N)   * cote, height/2+(i-N)   * cote,
                        width/2+(j-N+2) * cote, height/2+(i-N+1) * cote
                    ),
                    fill    = (255, ((i+j)%2)*255, 0),
                    outline = (  0, 0, 0),
                    width   = 0
                )

            if (dominos[i][j]==2):
                draw.rectangle(
                    (
                        width/2+(j-N)   * cote, height/2+(i-N)   * cote,
                        width/2+(j-N+1) * cote, height/2+(i-N+2) * cote
                    ),
                    fill    = (  0, ((i+j)%2)*255, 255),
                    outline = (  0,   0,   0),
                    width   = 0
                )

def iteration(dom, n):
    M=n+1
    copydom = [ [0 for i in range(2*M)] for j in range(2*M) ]
    for i in range(2*n):
        for j in range(2*n):
            copydom[i+1][j+1] = dom[i][j]

    resultat = [ [0 for i in range(2*M)] for j in range(2*M) ]
    for i in range(2*M-1):
        for j in range(2*M-1):
            if ((i+j+M+1)%2==0):
                if (copydom[i][j]==1):
                    if (copydom[i+1][j]!=1):
                        resultat[i+1][j]=1
                if (copydom[i][j]==2):
                    if (copydom[i][j+1]!=2):
                        resultat[i][j+1]=2
                if (copydom[i][j]==0):
                    if (copydom[i+1][j]==1):
                        resultat[i][j]=1
                    elif (copydom[i][j+1]==2):
                        resultat[i][j]=2
                    else:
                        if ((abs(M-0.5-i)+abs(M-0.5-j)<=M) and (i+j<3*M-1)):
                            if (random.random()>0.5):
                                resultat[i][j]=1
                                resultat[i+1][j]=1
                            else:
                                resultat[i][j]=2
                                resultat[i][j+1]=2
    return resultat

for k in range(200):
    dominos = iteration(dominos, N)
    N = N + 1

cote = math.floor(width/(2*N)*0.95)

traceDominos()

image.show()