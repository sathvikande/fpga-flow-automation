FPGA Design Flow Automation using Python & TCL
Overview

This project demonstrates automation of the complete FPGA design flow in Vivado using Python and TCL scripting.

Instead of manually running simulation, synthesis, and implementation through the GUI, this framework executes the entire flow in batch mode using a single Python script.

The automation performs:

Simulation

Waveform generation

Synthesis

Place & Route

Timing analysis

Resource utilization extraction

Worst Negative Slack (WNS) extraction

Automatic waveform GUI launch

Features

Automated project creation

Batch-mode execution of Vivado

Functional simulation

Waveform database generation (.wdb)

Synthesis & Implementation

Timing report generation

Automatic extraction of:

Slice LUTs

Slice Registers

Worst Negative Slack (WNS)

Clean console summary output

Tools Used

Vivado 2018.3

Python 3.x

TCL scripting

XSIM simulator

Flow Architecture

Python Script (full_flow.py)
↓
Vivado Batch Mode
↓
Simulation
↓
Synthesis
↓
Implementation (Place & Route)
↓
Timing Report Generation
↓
Report Parsing (Python)
↓
Waveform GUI Launch

Project Structure

fpga-flow-automation/
│
├── flow.tcl
├── full_flow.py
├── top.v
├── tb.v
├── README.md
└── screenshots/
├── waveform.png
└── summary_output.png

Sample Console Output

Flow completed successfully
Slice Registers Used: 4
Worst Negative Slack (WNS): 1.0 ns
Timing Status: PASS

Waveform Output

The waveform shows:

Clock toggling correctly

Reset behavior

4-bit counter incrementing sequentially

Key Learning Outcomes

Understanding of Vivado batch mode execution

TCL scripting for EDA tool control

Static Timing Analysis (STA)

Slack & Worst Negative Slack (WNS) concepts

Automated report parsing

Difference between GUI-driven and scripted design flows

Debugging and flow engineering mindset

How to Run

Install Vivado (update the Vivado path inside full_flow.py)

Make sure Python 3.x is installed

Run:

python full_flow.py

The script will:

Run simulation

Generate waveform

Perform synthesis and implementation

Extract timing and utilization metrics

Open waveform viewer automatically

Future Improvements

Multi-design regression testing

Automatic pass/fail timing detection

Timing constraint sweep automation

CSV report generation

Continuous Integration (CI) support

Author

Built as a learning project to explore FPGA flow automation and EDA scripting concepts.

You can paste this directly — no edits needed.
