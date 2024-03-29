#!/bin/bash
petalinux-create -t project -s ./u96v2_sbc_base_2020_2.bsp
cd u96v2_sbc_base_2020_2
petalinux-config --get-hw-description ../bd_wrapper.xsa
#petalinux-config
#petalinux-config -c rootfs
#petalinux-config -c kernel
#petalinux-build 
cp ../petalinuxbsp.conf ./project-spec/meta-user/conf
cp ../system-user.dtsi ./project-spec/meta-user/recipes-bsp/device-tree/files
petalinux-build -c avnet-image-full
petalinux-build --sdk
petalinux-package --sysroot
cd /images/linux
petalinux-package --boot --fsbl zynqmp_fsbl.elf --u-boot u-boot.elf --pmufw pmufw.elf --fpga system.bit
petalinux-boot --qemu --prebuilt 3
