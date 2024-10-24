############################################################
## This file is generated automatically by Vitis HLS.
## Please DO NOT edit it.
## Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
############################################################
open_project img_averaging_prj
set_top krnl_img_averaging
add_files img_averaging.cpp
add_files img_averaging.h
add_files -tb img_averaging_tb.cpp
open_solution "solution1" -flow_target vitis
set_part {xczu3eg-sbva484-1-e}
create_clock -period 10 -name default
config_interface -m_axi_alignment_byte_size 64 -m_axi_latency 64 -m_axi_max_widen_bitwidth 512 -m_axi_offset slave
config_rtl -register_reset_num 3
source "./directives.tcl"
csim_design
csynth_design
cosim_design
config_export -format xo -output ./
export_design -rtl verilog -format xo -output ./
