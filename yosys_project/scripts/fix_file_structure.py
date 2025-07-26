import os
import shutil

# Define directories
BASE_DIR = os.path.expanduser("~/yosys_project")
SCRIPT_DIR = os.path.join(BASE_DIR, "scripts")
VERILOG_DIR = os.path.join(BASE_DIR, "verilog_files")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
SYNTHESIS_DIR = os.path.join(RESULTS_DIR, "synthesis_reports")
NETLIST_DIR = os.path.join(RESULTS_DIR, "netlists")
LOGS_DIR = os.path.join(RESULTS_DIR, "logs")
YOSYS_DIR = os.path.join(BASE_DIR, "yosys")
LIBERTY_DIR = os.path.join(BASE_DIR, "liberty")
MISC_DIR = os.path.join(BASE_DIR, "misc")

# Ensure directories exist
for directory in [SCRIPT_DIR, VERILOG_DIR, RESULTS_DIR, SYNTHESIS_DIR, NETLIST_DIR, LOGS_DIR, YOSYS_DIR, LIBERTY_DIR, MISC_DIR]:
    os.makedirs(directory, exist_ok=True)

# Move files
file_movements = {
    "extract_rtl_features.py": SCRIPT_DIR,
    "synthesis_script.ys": SCRIPT_DIR,
    "rtl_combinational_de*": RESULTS_DIR,
    "wget-log*": MISC_DIR,
}

for file_pattern, target_dir in file_movements.items():
    for file_path in os.popen(f'ls ~/{file_pattern}').read().split("\n"):
        if file_path.strip():
            try:
                shutil.move(file_path.strip(), target_dir)
                print(f"Moved {file_path.strip()} to {target_dir}")
            except Exception as e:
                print(f"Error moving {file_path.strip()}: {e}")

print("File organization completed!")
