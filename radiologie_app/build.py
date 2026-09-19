import subprocess

def build():
    print("Démarrage de la compilation PyInstaller...")
    cmd = [
        "pyinstaller",
        "--noconsole",
        "--onefile",
        "--name=MedicalRadiologyAI",
        "--add-data=frontend;frontend",
        "main.py"
    ]
    subprocess.run(cmd, check=True)
    print("\nCompilation terminée. Votre .exe est dans le dossier 'dist/'.")

if __name__ == "__main__":
    build()