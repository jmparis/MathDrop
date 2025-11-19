#!/bin/bash
set -e

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Erreur : python3 n'est pas installé."
    exit 1
fi

# Check if the venv module is available
if ! python3 -c "import venv" &> /dev/null; then
    echo "Erreur : Le module 'venv' n'est pas installé."
    echo "Sur les systèmes Debian/Ubuntu, essayez : sudo apt install python3-venv"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Création de l'environnement virtuel dans .venv..."
    python3 -m venv .venv
else
    echo "L'environnement virtuel existe déjà."
fi

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
echo "Mise à jour de pip..."
pip install --upgrade pip

# Install dependencies from requirements.txt
if [ -f requirements.txt ]; then
    echo "Installation des dépendances..."
    pip install -r requirements.txt
else
    echo "Aucun fichier requirements.txt trouvé."
fi

echo "Configuration terminée."
