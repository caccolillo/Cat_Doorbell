#!/bin/bash
#download the dpu project
wget -O ./dpu.tar.gz https://www.xilinx.com/bin/public/openDownload?filename=DPUCZDX8G_VAI_v3.0.tar.gz
#extract it
tar -xvzf dpu.tar.gz
#replace the needed tcl files
cp ./trd_prj.tcl ./DPUCZDX8G_VAI_v3.0/prj/Vivado/hw/scripts/trd_prj.tcl
cp ./trd_bd.tcl ./DPUCZDX8G_VAI_v3.0/prj/Vivado/hw/scripts/base/trd_bd.tcl
#launch vivado to build the project
vivado -mode batch -source DPUCZDX8G_VAI_v3.0/prj/Vivado/hw/scripts/trd_prj.tcl&
#
