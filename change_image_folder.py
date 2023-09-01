import os
import shutil

# Define the source and destination directories
src_dir = os.path.join('inference', 'results', 'restored_faces')
crp_dir = os.path.join('inference', 'results', 'cropped_faces')
dest_dir = os.path.join('final_inference', 'DR')
cropps_dir = os.path.join('final_inference', 'DR_crop')

# If the destination directory exists, remove its contents
if os.path.exists(dest_dir):
    for filename in os.listdir(dest_dir):
        filepath = os.path.join(dest_dir, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)
else:
    # If the destination directory doesn't exist, create it
    os.makedirs(dest_dir)
    
# If the destination directory exists, remove its contents
if os.path.exists(cropps_dir):
    for filename in os.listdir(cropps_dir):
        filepath = os.path.join(cropps_dir, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)
else:
    # If the destination directory doesn't exist, create it
    os.makedirs(cropps_dir)

# Iterate through all files in the source directory and copy them to the destination
for filename in os.listdir(src_dir):
    filepath = os.path.join(src_dir, filename)
    if os.path.isfile(filepath):
        shutil.copy2(filepath, dest_dir)
        
for filename in os.listdir(crp_dir):
    filepath = os.path.join(crp_dir, filename)
    if os.path.isfile(filepath):
        shutil.copy2(filepath, cropps_dir)

print(f"Enhancing the image...")