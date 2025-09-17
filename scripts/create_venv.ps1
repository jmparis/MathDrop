# Create a virtual environment in .venv
python -m venv .venv

# Activate the virtual environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies from requirements.txt
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
}
