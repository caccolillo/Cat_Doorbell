#!/bin/bash
source /home/caccolillo/Xilinx/settings.sh
petalinux-create -t project -s u96v2_sbc_base_2022_2.bsp --name petalinux_prj
cd petalinux_prj
petalinux-config --get-hw-description ../bd_wrapper.xsa
petalinux-config
petalinux-config -c rootfs
petalinux-config -c kernel
#petalinux-boot –-jtag –-fpga
#petalinux-boot --jtag --fpga --bitstream ./images/linux/system.bit --u-boot
#petalinux-boot –-jtag –-kernel
#petalinux-build
petalinux-build -c petalinux-image-minimal
#petalinux-build -c petalinux-image-full
cd /images/linux
petalinux-package --boot --fsbl zynqmp_fsbl.elf --u-boot u-boot.elf --pmufw pmufw.elf --fpga system.bit
