import os
import subprocess

# Path to Inference
path_to_inference = "./inference"

# Change the current directory to Inference
os.chdir(path_to_inference)

# Run setup.py
try:
    subprocess.check_call(["python", "setup.py", "develop"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.CalledProcessError as e:
    print("Output:", e.output)
    print("Error:", e.stderr)

# Remove any existing results
print("Cleaning up old results ...")
subprocess.check_call(["rm", "-rf", "results"])

# Run inference
print("Running inference ...")
subprocess.check_call(["python", "inference.py", "-i", "inputs/upload", "-o", "results", "-v", "1.3", "-s", "2", "--bg_upsampler", "realesrgan"])

# Change the directory back to the original
os.chdir("..")
print('Changing directory')
subprocess.check_call(["python", "change_image_folder.py"])

# Path to final inference
path_to_final = './final_inference'
os.chdir(path_to_final)

# Run Final Inference
print('Running inference ...')
subprocess.check_call(["python", "degradation_removal.py"])
subprocess.check_call(["python", "demo.py", "--task", "FaceEnhancement", "--model", "GPEN-BFR-512", "--in_size", "512", "--channel_multiplier", "2", "--narrow", "1", "--use_sr", "--sr_scale", "2", "--use_cuda", "--save_face", "--indir", "DR", "--outdir", "results"])

print("Done")