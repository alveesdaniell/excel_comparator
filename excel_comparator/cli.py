import os
import sys
import subprocess

def main():
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller: caminho temporário onde os arquivos são extraídos
        base_path = sys._MEIPASS
    else:
        # Execução normal
        base_path = os.path.dirname(os.path.abspath(__file__))

    app_path = os.path.join(base_path, "app.py")

    # Garantir que o argumento da porta seja passado corretamente
    sys.argv = ["streamlit", "run", app_path, "--server.port=8501"]

    # Usando subprocess para chamar o streamlit e passar os parâmetros corretamente
    subprocess.run(sys.argv)

if __name__ == "__main__":
    main()
