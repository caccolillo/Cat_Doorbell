#!/bin/bash
petalinux-create --type project --template zynqMP --name ultra96
cd ultra96
petalinux-config --get-hw-description ../bd_wrapper.xsa
rm ./project-spec/configs/config
cp ../config ./project-spec/configs
#cp ../system-user.dtsi ./project-spec/meta-user/recipes-bsp/device-tree/files
cp ../petalinuxbsp.conf ./project-spec/meta-user/conf
cp ../wired.network ./project-spec/configs/systemd-conf
petalinux-build 
petalinux-build --sdk
petalinux-package --sysroot
cd images/linux
petalinux-package --boot --fsbl zynqmp_fsbl.elf --u-boot u-boot.elf --pmufw pmufw.elf --fpga system.bit
petalinux-boot --qemu --prebuilt 3
#sudo fdisk -l
#dd if=./rootfs.ext4 of=/dev/sdb2 status=progress


