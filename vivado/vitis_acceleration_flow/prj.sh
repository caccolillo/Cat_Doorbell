#!/bin/bash
# Execute Vivado in batch mode to build the hardware project and xsa
# file

rm -r ./myproj
rm *.log
rm *.jou

vivado -mode batch -source prj.tcl
