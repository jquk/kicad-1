import os
import subprocess
from pathlib import Path

# Define the folder path containing your old Kicad symbol files that have '.dcm' and '.lib' extension
input_path = None #"/path/to/the/kicad-library-symbols/"

# Convert to a clean Path object if the string is populated
input_path_object = Path(input_path) if input_path else None

# Check 1: Ensure the variable isn't empty and points to an actual directory
if not input_path_object or not input_path_object.is_dir():
    print(f"Error: '{input_path}' is not a valid directory path.")
    print("Please fix the 'input_path' variable at the top of the script.")
    exit(1)

# Check 2: Scan for any legacy KiCad symbol files (.lib or .dcm)
# rglob finds matching extensions anywhere in the directory or its subfolders
legacy_files = [
    f for f in input_path_object.rglob("*") 
    if f.suffix.lower() in [".lib", ".dcm"]
]

if not legacy_files:
    print(f"Error: No legacy KiCad symbol files (.lib or .dcm) found inside '{input_path}'.")
    print("Please verify the directory contents.")
    exit(1)

# Success confirmation
print(f"Success: Validated folder. Found {len(legacy_files)} legacy file(s) ready to upgrade.")

# Now upgrade the old Kicad symbol files to the new format 
for file_name in os.listdir(input_path):
    if file_name.endswith(".lib"):
        lib_path = os.path.join(input_path, file_name)
        new_name = file_name.replace(".lib", ".kicad_sym")
        output_path = os.path.join(input_path, new_name)
        
        print(f"Upgrading {file_name}...")
        # Note the fix here: "upgrade" instead of "convert"
        subprocess.run(["kicad-cli", "sym", "upgrade", "--output", output_path, lib_path])

print("Batch conversion completed successfully!")

