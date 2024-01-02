############################################################
## This file is generated automatically by Vitis HLS.
## Please DO NOT edit it.
## Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
############################################################
open_project img_averaging_prj
set_top img_averaging
add_files img_averaging.cpp
open_solution "solution1" -flow_target vitis
set_part {xczu3eg-sbva484-1-e}
create_clock -period 10 -name default
#source "./img_averaging_prj/solution1/directives.tcl"
#csim_design
csynth_design
#cosim_design
export_design -format ip_catalog
