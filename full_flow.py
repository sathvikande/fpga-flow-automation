import subprocess
import os
import glob

vivado_path = r"C:\Xilinx\Vivado\2018.3\bin\vivado.bat"

design="top.v"
testbench="tb.v"

for file in ["util_report.txt", "timing_report.txt"]:
    if os.path.exists(file):
        os.remove(file)
        
command =[
    vivado_path,
    "-mode",
    "batch",
    "-source",
    "flow.tcl",
    "-tclargs",
    design,
    testbench
    ]
    
result=subprocess.run(
    command,
    capture_output=True,
    text=True,
    shell=True,
    )
    
with open("full_flow.log","w") as f:
        f.write(result.stdout)
        
if result.returncode !=0:
   print("flow failed")
   print(result.stdout)
else:
     print("flow compeleted successfully");

if os.path.exists("util_report.txt"):
    with open("util_report.txt","r") as f:
        report=f.readlines()
        
    for line in report:
        if "Slice LUTS" in line:
            print("LUT Usage", line.strip())
        if "Slice Registers" in line:
            print("Register usage:", line.strip())
            
if os.path.exists("timing_report.txt"):
    with open("timing_report.txt","r") as f:
        for line in f:
            if "WNS" in line:
                print("Timing Info :", line.strip())
                
     
wns_value = None

if os.path.exists("timing_report.txt"):
    with open("timing_report.txt", "r") as f:
        for line in f:
            # Skip header lines
            if "WNS(ns)" in line:
                continue

            parts = line.strip().split()

            # Check if first token is a valid float
            if len(parts) > 0:
                try:
                    value = float(parts[0])
                    # WNS values are typically small numbers like 3.421 or -0.123
                    if -100.0 < value < 100.0:
                        wns_value = value
                        break
                except:
                    continue

if wns_value is not None:
    print("\nWorst Negative Slack (WNS):", wns_value, "ns")
else:
    print("\nCould not extract WNS value.")

if os.path.exists("wave.vcd"):
    print("waveform is generated successfully")
    
    
  

# Find generated waveform file
wdb_files = glob.glob("auto_proj/**/*.wdb", recursive=True)

if wdb_files:
    wdb_file = wdb_files[0]
    print("\nOpening waveform viewer...")

    xsim_path = r"C:\Xilinx\Vivado\2018.3\bin\xsim.bat"

    subprocess.Popen([xsim_path, wdb_file, "-gui"], shell=True)
else:
    print("\nWaveform file not found.")