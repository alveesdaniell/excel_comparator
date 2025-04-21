import subprocess
import sys

def main():
    try:
        subprocess.check_call([sys.executable, "-m", "streamlit", "run", "app.py"])
    except Exception as e:
        print(f"Erro ao executar: {e}")
        print("Instale as dependências com:")
        print("python -m pip install streamlit pandas openpyxl xlsxwriter")

if __name__ == "__main__":
    main()