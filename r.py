import sys
import subprocess
import os

def add_gpp_to_path():
    gpp_path = r"C:\\msys64\\ucrt64\\bin"

    current_path = os.environ.get("PATH", "")

    if gpp_path not in current_path:
        # Add the path to PATH
        os.environ["PATH"] = f"{gpp_path};{current_path}"

    result = subprocess.run(["g++", "--version"], capture_output=True, text=True)
    if result.returncode != 0:
        print("g++ is still not recognized. Make sure the path is correct and g++ is installed.")

def compile_and_run_cpp(file_name):
    if not os.path.isfile(file_name):
        print(f"Error: File '{file_name}' not found.")
        return

    executable = "output.exe" if os.name == "nt" else "output"
    compile_command = ["g++", "-std=c++23", "-o", executable, file_name]
    try:
        subprocess.run(compile_command, check=True)
    except subprocess.CalledProcessError:
        print("Compilation failed.")
        return

    run_command = [f"./{executable}"] if os.name != "nt" else [executable]
    try:
        subprocess.run(run_command, check=True)
    except subprocess.CalledProcessError:
        print("Execution failed.")

if __name__ == "__main__":
    add_gpp_to_path()
    subprocess.run("cls", shell=True)
    if len(sys.argv) < 2:
        cpp_files = [f for f in os.listdir('.') if f.endswith('.cpp')]

        if len(cpp_files) == 1:
            compile_and_run_cpp(cpp_files[0])
        elif len(cpp_files) == 0:
            print("Error: No .cpp files found in the current directory.")
        else:
            print("Error: Multiple .cpp files found in the current directory. Please specify one as an argument.")
    else:
        compile_and_run_cpp(sys.argv[1])
