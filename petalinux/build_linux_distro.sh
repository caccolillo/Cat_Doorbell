#!/bin/bash
source /home/caccolillo/Documents/Xilinx/petalinux/settings.sh
petalinux-create -t project --template zynqMP --name petalinux_prj
cd petalinux_prj
petalinux-config --get-hw-description ../bd_wrapper.xsa
petalinux-config
petalinux-config -c rootfs
petalinux-config -c kernel
petalinux-build 
petalinux-build --sdk
petalinux-package --sysroot
cd /images/linux
petalinux-package --boot --fsbl zynqmp_fsbl.elf --u-boot u-boot.elf --pmufw pmufw.elf --fpga system.bit
