import os
import subprocess

# Define the folder containing your old .lib files
input_folder = "/path/to.../digikey-kicad-library-master/digikey-symbols"

for file_name in os.listdir(input_folder):
    if file_name.endswith(".lib"):
        lib_path = os.path.join(input_folder, file_name)
        new_name = file_name.replace(".lib", ".kicad_sym")
        output_path = os.path.join(input_folder, new_name)
        
        print(f"Upgrading {file_name}...")
        # Note the fix here: "upgrade" instead of "convert"
        subprocess.run(["kicad-cli", "sym", "upgrade", "--output", output_path, lib_path])

print("Batch conversion completed successfully!")

