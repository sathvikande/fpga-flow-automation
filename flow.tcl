set design_file [lindex $argv 0]
set tb_file [lindex $argv 1]

create_project auto_proj ./auto_proj -part xc7a35tcpg236-1 -force

add_files $design_file
add_files -fileset sim_1 $tb_file

update_compile_order -fileset sources_1
update_compile_order -fileset sim_1

# -----------------
# Simulation
# -----------------
launch_simulation

add_wave -recursive *
run 200ns

close_sim

# -----------------
# Synthesis
# -----------------
synth_design -top top
report_utilization -file util_report.txt

opt_design
place_design
route_design

report_timing_summary -file timing_report.txt

exit

restart
run 200ns