import math
from PIL import Image, ImageDraw
from pathlib import Path

width = 5000
height = 5000

image = Image.new("RGB", (width, height), (0, 0, 0))
draw = ImageDraw.Draw(image)

P0 = [width / 2 + 400, height / 2 + 700]
dir = [-1, 0]
L = 1
plis = [1]  # 1 -> droite, -1 --> gauche


def deplie():
    l = len(plis)
    plis.append(1)
    for i in range(l):
        plis.append(-plis[l - 1 - i])


def trace():
    d = dir
    P = P0
    Q = [P[0] + L * d[0], P[1] + L * d[1]]
    draw.line((P, Q), fill=(0, 0, 0), width=1)
    for i in range(len(plis)):
        d = [d[1] * plis[i], -d[0] * plis[i]]
        P = Q
        Q = [P[0] + L * d[0], P[1] + L * d[1]]
        couleur = math.floor(i / len(plis) * 255)
        draw.line((P, Q), fill=(couleur, 255 - couleur, 70), width=1)


for i in range(22):
    deplie()

# print(plis)

trace()
image.show()
