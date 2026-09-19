import sys
import os
import webview
from backend.api import MedicalApi

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def main():
    api = MedicalApi()
    html_file = get_resource_path(os.path.join("frontend", "index.html"))

    window = webview.create_window(
        title="Système Sécurisé - Analyse Radiologie",
        url=html_file,
        js_api=api,
        width=850,
        height=720,
        resizable=False
    )
    webview.start()

if __name__ == "__main__":
    main()