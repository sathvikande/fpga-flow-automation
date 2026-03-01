FPGA Design Flow Automation using Python & TCL
📌 Overview

This project demonstrates automation of the complete FPGA design flow in Vivado using Python and TCL scripting.

Instead of manually running simulation, synthesis, and implementation through the GUI, this framework executes the entire flow in batch mode using a single Python script.

🚀 Features

Automated project creation

Simulation execution

Waveform generation

Synthesis

Place & Route

Timing analysis

Automatic extraction of:

Slice LUTs

Slice Registers

Worst Negative Slack (WNS)

Automatic waveform GUI launch

🛠 Tools Used

Vivado 2018.3

Python 3.x

TCL scripting

XSIM simulator

🔁 Flow Architecture
Python Script
     ↓
Vivado Batch Mode
     ↓
Simulation
     ↓
Synthesis
     ↓
Implementation
     ↓
Timing Report Generation
     ↓
Report Parsing (Python)
📊 Sample Output
Flow completed successfully
Slice Registers Used: 4
Worst Negative Slack (WNS): 1.0 ns
Timing Status: PASS
📷 Waveform Output

Counter simulation waveform:

(Insert waveform screenshot here)

📂 File Description

full_flow.py → Python automation script

flow.tcl → TCL script controlling Vivado

top.v → RTL design (4-bit counter)

tb.v → Testbench

🎯 Learning Outcomes

Understanding of batch-mode FPGA flows

Static Timing Analysis (WNS extraction)

Report parsing automation

Difference between GUI and scripted flows

Flow debugging and tool control

▶ How to Run

Install Vivado

Update Vivado path in full_flow.py

Run:

python full_flow.py
📌 Future Improvements

Multi-design regression support

Automatic pass/fail detection

Timing constraint sweep

CSV report generation
