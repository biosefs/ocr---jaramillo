import subprocess

try:
    result = subprocess.run(['java', '-version'], capture_output=True, text=True)
    print("Java is installed and in PATH:")
    print(result.stderr.splitlines()[0])
except FileNotFoundError:
    print("Java not found in PATH. Please install Java and add it to your PATH.")