import os

sv_dir = "/home/yashigauri/yosys_project/scripts/Verilog_Dataset"  # ✅ Corrected path

if os.path.exists(sv_dir):
    files = os.listdir(sv_dir)
    print(f"✅ Directory exists: {sv_dir}")
    print(f"📂 Files inside: {files}")
    if not files:
        print("⚠️ No Verilog files found!")
else:
    print(f"❌ Directory NOT found: {sv_dir}")

