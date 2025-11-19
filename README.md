# MathDrop
Programs coded during the Micmaths live sessions, on his MathsDrop YT channel

## Project Structure

This repository contains several mathematical examples, each in its own folder:

- `01 - L'Échiquier inversé/` — Inverse chessboard example
- `02 - 2 Modulo 131/` — Modulo 131 example
- `03 - Pavage de flocons de Koch/` — Koch snowflake tiling
- `04 - Pythagore/` — Pythagorean example
- `05 - Les lacs de Wada/` — Wada lakes fractal visualization
- `06 - Poursuite/` — Pursuit curve simulation
- `07 - Nopertedre/` — POV-Ray 3D rendering project

Each example is self-contained and can be run independently.

## Scripts

The `scripts/` folder contains utility scripts for managing the development environment:

- **`create_venv.sh`** — Creates and configures a Python virtual environment (Linux/macOS)
- **`create_venv.ps1`** — Creates and configures a Python virtual environment (Windows PowerShell)
- **`clean.sh`** — Cleans the repository by removing temporary files, caches, and the virtual environment (Linux/macOS)
- **`clean.ps1`** — Cleans the repository by removing temporary files, caches, and the virtual environment (Windows PowerShell)


## Setup

1. Create and activate a virtual environment:
   - **Linux/macOS**: `./scripts/create_venv.sh`
   - **Windows PowerShell**: `.\scripts\create_venv.ps1`
2. All Python dependencies are listed in `requirements.txt` at the project root.

## Running Examples

Navigate to the desired example folder and run the corresponding Python script. For example:

```bash
cd "06 - Poursuite"
./launch.sh
```

Or run Python scripts directly:

```bash
cd "05 - Les lacs de Wada"
python wada.py
```

## Cleaning the Repository

To remove all temporary files, caches, and the virtual environment:

- **Linux/macOS**: `./scripts/clean.sh`
- **Windows PowerShell**: `.\scripts\clean.ps1`


This will clean up:
- Python virtual environment (`.venv`)
- Python cache files (`__pycache__`, `*.pyc`)
- Test and coverage files
- IDE configuration files
- Generated images in `pictures/`
- Log files and other temporary files

After cleaning, you can recreate the environment with `./scripts/create_venv.sh`.

---

Feel free to explore each folder for code and visualizations!
