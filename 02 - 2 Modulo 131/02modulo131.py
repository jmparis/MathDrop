# https://www.youtube.com/watch?v=nwmuSzFXd8M
import math
from PIL import Image, ImageDraw
from pathlib import Path

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

def find_project_root(start_path: Path, marker: str = "requirements.txt") -> Path:
    for parent in [start_path] + list(start_path.parents):
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Could not find project root containing {marker}")

project_root = find_project_root(Path(__file__).resolve())
picture_path = project_root / "pictures" / "02modulo131.png"

multi.save(str(picture_path))
multi.show()
