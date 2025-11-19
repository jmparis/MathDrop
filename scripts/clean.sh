#!/bin/bash
set -e

echo "🧹 Nettoyage du repository MathDrop..."
echo ""

# Function to remove directory if it exists
remove_dir() {
    if [ -d "$1" ]; then
        echo "  ✓ Suppression de $1"
        rm -rf "$1"
    fi
}

# Function to remove files matching pattern
remove_files() {
    local pattern="$1"
    local description="$2"
    local count=$(find . -name "$pattern" 2>/dev/null | wc -l)
    if [ "$count" -gt 0 ]; then
        echo "  ✓ Suppression de $count fichier(s) $description"
        find . -name "$pattern" -type f -delete 2>/dev/null || true
    fi
}

# Remove Python virtual environment
echo "📦 Environnement virtuel Python:"
remove_dir ".venv"
remove_dir "venv"
remove_dir "env"
remove_dir "ENV"
remove_dir "env.bak"
remove_dir "venv.bak"

# Remove Python cache files
echo ""
echo "🐍 Fichiers Python compilés et cache:"
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
echo "  ✓ Suppression des répertoires __pycache__"
remove_files "*.pyc" "Python bytecode (.pyc)"
remove_files "*.pyo" "Python optimized (.pyo)"
remove_files "*.pyd" "Python dynamic module (.pyd)"
remove_files "*\$py.class" "Python class files"

# Remove Python distribution/packaging files
echo ""
echo "📦 Fichiers de distribution/packaging:"
remove_dir "build"
remove_dir "dist"
remove_dir "*.egg-info"
remove_dir ".eggs"
remove_files "*.egg" "egg files"

# Remove test and coverage files
echo ""
echo "🧪 Fichiers de tests et couverture:"
remove_dir ".pytest_cache"
remove_dir ".coverage"
remove_dir "htmlcov"
remove_dir ".tox"
remove_dir ".nox"
remove_dir ".hypothesis"
remove_files "coverage.xml" "coverage XML"
remove_files "nosetests.xml" "nosetests XML"
remove_files ".coverage.*" "coverage data"

# Remove cache directories
echo ""
echo "💾 Répertoires de cache:"
remove_dir ".cache"
remove_dir ".mypy_cache"
remove_dir ".ruff_cache"
remove_dir ".pytype"
remove_dir ".dmypy.json"
remove_files "dmypy.json" "dmypy JSON"

# Remove IDE and editor files
echo ""
echo "💻 Fichiers IDE/éditeur:"
remove_dir ".ipynb_checkpoints"
remove_dir ".vscode"
remove_dir ".idea"
remove_dir ".spyderproject"
remove_dir ".spyproject"
remove_dir ".ropeproject"

# Remove log files
echo ""
echo "📝 Fichiers de log:"
remove_files "*.log" "log"
remove_files "pip-log.txt" "pip log"

# Remove generated pictures
echo ""
echo "🖼️  Images générées:"
if [ -d "pictures" ]; then
    local pic_count=$(find pictures -type f 2>/dev/null | wc -l)
    if [ "$pic_count" -gt 0 ]; then
        echo "  ✓ Suppression de $pic_count image(s) dans pictures/"
        rm -rf pictures/*
    else
        echo "  ℹ️  Aucune image à supprimer"
    fi
else
    echo "  ℹ️  Répertoire pictures/ n'existe pas"
fi

# Remove other temporary files
echo ""
echo "🗑️  Autres fichiers temporaires:"
remove_files "*.tmp" "temporary"
remove_files "*.temp" "temp"
remove_files "*~" "backup (~)"
remove_files ".DS_Store" "macOS metadata"

echo ""
echo "✨ Nettoyage terminé !"
echo ""
echo "💡 Pour recréer l'environnement virtuel, exécutez:"
echo "   ./scripts/create_venv.sh"
