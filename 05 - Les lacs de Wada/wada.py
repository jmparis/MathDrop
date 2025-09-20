# https://www.youtube.com/watch?v=DAelZCLyYjM
import math
from PIL import Image, ImageDraw
from pathlib import Path

width  = 1748
height = 1240
wada = Image.new("RGB", (width, height), (255, 255, 255))

u = 600

def newton():
    for x in range(width):
        for y in range(height):
            z = complex((x - width/2 - 300) / u, (y - height/2) / u)    
            for k in range(20):
                if (z != 0):
                    z = z - (z**3 - 2) / (3 * z**2)
            if (z.real > 0):
                wada.putpixel((x, y), (255, 0, 0))
            else:
                if (z.imag > 0):
                    wada.putpixel((x, y), (0, 255, 0))
                else:
                    wada.putpixel((x, y), (0, 0, 255))

newton()

def find_project_root(start_path: Path, marker: str = "requirements.txt") -> Path:
    for parent in [start_path] + list(start_path.parents):
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Could not find project root containing {marker}")

project_root = find_project_root(Path(__file__).resolve())
picture_path = project_root / "pictures" / "wada.png"

wada.save(str(picture_path))
wada.show()
