# https://www.youtube.com/watch?v=tHTuooDmOf8
import math
from PIL import Image, ImageDraw

width = 1748
height = 1240

poursuite = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(poursuite)

A = [100, 100]
B = [1000, 100]
C = [500, 800]

poly = [A, B, C]

def avance(P, Q, d):
    dist = math.sqrt((Q[0] - P[0])**2 + (Q[1] - P[1])**2)
    if dist < d:
        return Q
    else:
        return [P[0] + d * (Q[0] - P[0]) / dist, P[1] + d * (Q[1] - P[1]) / dist]

poursuite.show()
