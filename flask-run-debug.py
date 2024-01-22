import subprocess as sub
import os

CWD = os.getcwd()

if __name__ == "__main__":
	sub.run(CWD+r"\.venv\Scripts\python.exe -m flask --app "+CWD+r"\src\conta-papagne-app\conta-papagne.py run --debug")