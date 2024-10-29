
# Set the reference directory for source file relative paths (by default the value is script directory path)
set origin_dir "."

# Use origin directory path location variable, if specified in the tcl shell
if { [info exists ::origin_dir_loc] } {
  set origin_dir $::origin_dir_loc
}

# Set the project name
set _xil_proj_name_ "u96v2_dpu"

# Use project name variable, if specified in the tcl shell
if { [info exists ::user_project_name] } {
  set _xil_proj_name_ $::user_project_name
}

variable script_file
set script_file "dpu_ultra96.tcl"


# Create project
create_project ${_xil_proj_name_} ./${_xil_proj_name_} -part xczu3eg-sbva484-1-i

# Set the directory path for the new project
set proj_dir [get_property directory [current_project]]

# Set project properties
set obj [current_project]
set_property -name "board_part" -value "avnet.com:ultra96v2:part0:1.2" -objects $obj
set_property -name "default_lib" -value "xil_defaultlib" -objects $obj
set_property -name "enable_resource_estimation" -value "0" -objects $obj
set_property -name "enable_vhdl_2008" -value "1" -objects $obj
set_property -name "ip_cache_permissions" -value "read write" -objects $obj
set_property -name "ip_output_repo" -value "$proj_dir/${_xil_proj_name_}.cache/ip" -objects $obj
set_property -name "mem.enable_memory_map_generation" -value "1" -objects $obj
set_property -name "platform.board_id" -value "ultra96v2" -objects $obj
set_property -name "revised_directory_structure" -value "1" -objects $obj
set_property -name "sim.central_dir" -value "$proj_dir/${_xil_proj_name_}.ip_user_files" -objects $obj
set_property -name "sim.ip.auto_export_scripts" -value "1" -objects $obj
set_property -name "simulator_language" -value "Mixed" -objects $obj
set_property -name "sim_compile_state" -value "1" -objects $obj
set_property -name "xpm_libraries" -value "XPM_CDC" -objects $obj

# Create 'sources_1' fileset (if not found)
if {[string equal [get_filesets -quiet sources_1] ""]} {
  create_fileset -srcset sources_1
}

# Set IP repository paths

set_property  ip_repo_paths  ../ [current_project]
update_ip_catalog -rebuild

#create block design
source bd.tcl

#create and add the HDL wrapper
make_wrapper -files [get_files ./DPUCZDX8G_VAI_v3.0/prj/Vivado/hw/srcs/top/top.bd] -top
add_files -norecurse ./DPUCZDX8G_VAI_v3.0/prj/Vivado/hw/srcs/top/hdl/top_wrapper.v

#generate bitstream
launch_runs impl_1 -to_step write_bitstream -jobs 4

#create xsa file
write_hw_platform -fixed -include_bit -force -file ../../petalinux/top_wrapper.xsa



