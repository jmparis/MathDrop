# Create a virtual environment in .venv
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies from requirements.txt
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi
