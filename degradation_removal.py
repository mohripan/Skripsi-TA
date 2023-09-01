import os
import subprocess

# Path to Inference
path_to_inference = "./Degradation_Remover"

# Change the current directory to Inference
os.chdir(path_to_inference)

# Run Degradation Remover
print("Running degradation Removal")
subprocess.check_call(["python", "demo.py", "-i"])

print("Done")