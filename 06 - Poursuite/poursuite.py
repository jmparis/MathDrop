# https://www.youtube.com/watch?v=tHTuooDmOf8
import math
from PIL import Image, ImageDraw
from pathlib import Path

width = 1748
height = 1240

poursuite = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(poursuite)

A = [ 100,  100]
B = [ 100, 1100]
C = [1100, 1100]
D = [1100,  100]
poly = [A, B, C, D]

def avance(P, Q, d):
    dist = math.sqrt((Q[0] - P[0])**2 + (Q[1] - P[1])**2)
    if dist < d:
        return Q
    else:
        return [P[0] + d * (Q[0] - P[0]) / dist, P[1] + d * (Q[1] - P[1]) / dist]

def trace_poly(poly):
    for i in range(len(poly)):
        P = poly[i]
        Q = poly[(i+1) % len(poly)]
        draw.line((P[0], P[1], Q[0], Q[1]), fill=(0, 0, 0), width=2)

for k in range(200):
    trace_poly(poly)
    P0 = poly[0]
    for i in range(len(poly)-1):
        poly[i] = avance(poly[i], poly[i+1], math.dist(poly[i], poly[i+1]) / 10)
    poly[len(poly)-1] = avance(poly[len(poly)-1], P0, math.dist(poly[len(poly)-1], P0) / 10)


def find_project_root(start_path: Path, marker: str = "requirements.txt") -> Path:
    for parent in [start_path] + list(start_path.parents):
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Could not find project root containing {marker}")

project_root = find_project_root(Path(__file__).resolve())
picture_path = project_root / "pictures" / "poursuite.png"

poursuite.save(str(picture_path))

poursuite.show()
