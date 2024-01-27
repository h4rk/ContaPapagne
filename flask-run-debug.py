import subprocess as sub
import os

CWD = os.getcwd()

if __name__ == "__main__":
  
    python_exe = f'"{os.path.join(CWD, ".venv", "Scripts", "python.exe")}"'
    flask_app = f'"{os.path.join(CWD, "src", "ContaPapagneApp", "conta_papagne.py")}"'
    command = [python_exe, "-m", "flask", "--app", flask_app, "run", "--debug"]
    
    # Use shell=True to handle spaces in paths correctly on Windows
    sub.run(' '.join(command), shell=True)