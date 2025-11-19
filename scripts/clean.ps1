# Script de nettoyage du repository MathDrop pour Windows PowerShell
# Supprime les fichiers temporaires, caches, et l'environnement virtuel Python

Write-Host "🧹 Nettoyage du repository MathDrop..." -ForegroundColor Cyan
Write-Host ""

# Function to remove directory if it exists
function Remove-DirectoryIfExists {
    param([string]$Path)
    if (Test-Path $Path) {
        Write-Host "  ✓ Suppression de $Path" -ForegroundColor Green
        Remove-Item -Path $Path -Recurse -Force -ErrorAction SilentlyContinue
    }
}

# Function to remove files matching pattern
function Remove-FilesPattern {
    param(
        [string]$Pattern,
        [string]$Description
    )
    $files = Get-ChildItem -Path . -Filter $Pattern -Recurse -File -ErrorAction SilentlyContinue
    if ($files.Count -gt 0) {
        Write-Host "  ✓ Suppression de $($files.Count) fichier(s) $Description" -ForegroundColor Green
        $files | Remove-Item -Force -ErrorAction SilentlyContinue
    }
}

# Remove Python virtual environments
Write-Host "📦 Environnement virtuel Python:" -ForegroundColor Yellow
Remove-DirectoryIfExists ".venv"
Remove-DirectoryIfExists "venv"
Remove-DirectoryIfExists "env"
Remove-DirectoryIfExists "ENV"
Remove-DirectoryIfExists "env.bak"
Remove-DirectoryIfExists "venv.bak"

# Remove Python cache files
Write-Host ""
Write-Host "🐍 Fichiers Python compilés et cache:" -ForegroundColor Yellow
$pycacheDirs = Get-ChildItem -Path . -Filter "__pycache__" -Recurse -Directory -ErrorAction SilentlyContinue
if ($pycacheDirs.Count -gt 0) {
    Write-Host "  ✓ Suppression de $($pycacheDirs.Count) répertoire(s) __pycache__" -ForegroundColor Green
    $pycacheDirs | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
}
Remove-FilesPattern "*.pyc" "Python bytecode (.pyc)"
Remove-FilesPattern "*.pyo" "Python optimized (.pyo)"
Remove-FilesPattern "*.pyd" "Python dynamic module (.pyd)"

# Remove Python distribution/packaging files
Write-Host ""
Write-Host "📦 Fichiers de distribution/packaging:" -ForegroundColor Yellow
Remove-DirectoryIfExists "build"
Remove-DirectoryIfExists "dist"
$eggInfoDirs = Get-ChildItem -Path . -Filter "*.egg-info" -Recurse -Directory -ErrorAction SilentlyContinue
$eggInfoDirs | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Remove-DirectoryIfExists ".eggs"
Remove-FilesPattern "*.egg" "egg files"

# Remove test and coverage files
Write-Host ""
Write-Host "🧪 Fichiers de tests et couverture:" -ForegroundColor Yellow
Remove-DirectoryIfExists ".pytest_cache"
Remove-DirectoryIfExists ".coverage"
Remove-DirectoryIfExists "htmlcov"
Remove-DirectoryIfExists ".tox"
Remove-DirectoryIfExists ".nox"
Remove-DirectoryIfExists ".hypothesis"
Remove-FilesPattern "coverage.xml" "coverage XML"
Remove-FilesPattern "nosetests.xml" "nosetests XML"
$coverageFiles = Get-ChildItem -Path . -Filter ".coverage.*" -Recurse -File -ErrorAction SilentlyContinue
if ($coverageFiles.Count -gt 0) {
    Write-Host "  ✓ Suppression de $($coverageFiles.Count) fichier(s) coverage data" -ForegroundColor Green
    $coverageFiles | Remove-Item -Force -ErrorAction SilentlyContinue
}

# Remove cache directories
Write-Host ""
Write-Host "💾 Répertoires de cache:" -ForegroundColor Yellow
Remove-DirectoryIfExists ".cache"
Remove-DirectoryIfExists ".mypy_cache"
Remove-DirectoryIfExists ".ruff_cache"
Remove-DirectoryIfExists ".pytype"
Remove-FilesPattern "dmypy.json" "dmypy JSON"

# Remove IDE and editor files
Write-Host ""
Write-Host "💻 Fichiers IDE/éditeur:" -ForegroundColor Yellow
Remove-DirectoryIfExists ".ipynb_checkpoints"
Remove-DirectoryIfExists ".vscode"
Remove-DirectoryIfExists ".idea"
Remove-DirectoryIfExists ".spyderproject"
Remove-DirectoryIfExists ".spyproject"
Remove-DirectoryIfExists ".ropeproject"

# Remove log files
Write-Host ""
Write-Host "📝 Fichiers de log:" -ForegroundColor Yellow
Remove-FilesPattern "*.log" "log"
Remove-FilesPattern "pip-log.txt" "pip log"

# Remove generated pictures
Write-Host ""
Write-Host "🖼️  Images générées:" -ForegroundColor Yellow
if (Test-Path "pictures") {
    $picFiles = Get-ChildItem -Path "pictures" -File -ErrorAction SilentlyContinue
    if ($picFiles.Count -gt 0) {
        Write-Host "  ✓ Suppression de $($picFiles.Count) image(s) dans pictures/" -ForegroundColor Green
        $picFiles | Remove-Item -Force -ErrorAction SilentlyContinue
    } else {
        Write-Host "  ℹ️  Aucune image à supprimer" -ForegroundColor Gray
    }
} else {
    Write-Host "  ℹ️  Répertoire pictures/ n'existe pas" -ForegroundColor Gray
}

# Remove other temporary files
Write-Host ""
Write-Host "🗑️  Autres fichiers temporaires:" -ForegroundColor Yellow
Remove-FilesPattern "*.tmp" "temporary"
Remove-FilesPattern "*.temp" "temp"
Remove-FilesPattern "*~" "backup (~)"
Remove-FilesPattern ".DS_Store" "macOS metadata"

Write-Host ""
Write-Host "✨ Nettoyage terminé !" -ForegroundColor Green
Write-Host ""
Write-Host "💡 Pour recréer l'environnement virtuel, exécutez:" -ForegroundColor Cyan
Write-Host "   .\scripts\create_venv.ps1" -ForegroundColor White
