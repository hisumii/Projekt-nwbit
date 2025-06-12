if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python nie jest zainstalowany lub nie jest w PATH!"
    exit 1
}
pip install pyinstaller
pip install pyyaml
pip install xmltodict