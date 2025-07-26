import os
import subprocess
import re
import pandas as pd
import glob
import logging

BASE_DIR = os.path.expanduser("~/yosys_project")
SV_FILES_DIR = os.path.join(BASE_DIR, "scripts", "Verilog_Dataset")  
RESULTS_DIR = os.path.join(BASE_DIR, "results")
LOGS_DIR = os.path.join(RESULTS_DIR, "logs")
LIBERTY_FILE = os.path.join(BASE_DIR, "liberty_file.lib")
DATASET_PATH = os.path.join(RESULTS_DIR, "rtl_dataset.csv")

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, "yosys_logs.txt")
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_module_name(sv_file):
    with open(sv_file, 'r') as f:
        content = f.read()
    match = re.search(r'\bmodule\s+(\w+)', content)
    return match.group(1) if match else None

def run_yosys_synthesis(sv_file):
    module_name = get_module_name(sv_file)
    if not module_name:
        return None
    
    yosys_cmd = f"yosys -p 'read_verilog -sv {sv_file}; synth -top {module_name}; abc -liberty {LIBERTY_FILE}; stat'"
    result = subprocess.run(yosys_cmd, shell=True, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None

def extract_features(sv_file):
    with open(sv_file, 'r') as f:
        content = f.read()
    return {
        'file_name': os.path.basename(sv_file),
        'num_inputs': len(re.findall(r'input\s+\w+', content)),
        'num_outputs': len(re.findall(r'output\s+\w+', content)),
        'num_regs': len(re.findall(r'reg\s+\w+', content)),
        'num_wires': len(re.findall(r'wire\s+\w+', content)),
        'num_assigns': len(re.findall(r'assign\s+', content)),
        'num_always_blocks': len(re.findall(r'always\s+@', content)),
    }

def create_dataset():
    sv_files = glob.glob(os.path.join(SV_FILES_DIR, "*.sv")) + glob.glob(os.path.join(SV_FILES_DIR, "*.v"))  
    print(f"🔍 Found {len(sv_files)} Verilog files in {SV_FILES_DIR}: {sv_files}")

    if not sv_files:
        print("⚠️ No Verilog files found! Check the directory and extensions.")
        return

    dataset_rows = []
    
    for sv_file in sv_files:
        print(f"📂 Processing: {sv_file}")
        features = extract_features(sv_file)
        print(f"📊 Extracted features: {features}")
        dataset_rows.append(features)
    
    df = pd.DataFrame(dataset_rows)
    print(f"📋 DataFrame before saving:\n{df}")

    df.to_csv(DATASET_PATH, index=False)
    print(f"✅ Dataset saved at {DATASET_PATH}")

if __name__ == "__main__":
    create_dataset()

