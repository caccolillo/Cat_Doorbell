# Set the reference directory for source file relative paths (by default the value is script directory path)
set origin_dir "."

# Set the project name
set _xil_proj_name_ "ultra96_basic_system"


# Create project
create_project ${_xil_proj_name_} ./${_xil_proj_name_} -part xczu3eg-sbva484-1-i

# Set the directory path for the new project
set proj_dir [get_property directory [current_project]]

# Set project properties
set obj [current_project]
set_property -name "board_part" -value "avnet.com:ultra96v2:part0:1.2" -objects $obj
set_property -name "default_lib" -value "xil_defaultlib" -objects $obj
set_property -name "enable_vhdl_2008" -value "1" -objects $obj
set_property -name "ip_cache_permissions" -value "read write" -objects $obj
set_property -name "ip_output_repo" -value "$proj_dir/${_xil_proj_name_}.cache/ip" -objects $obj
set_property -name "mem.enable_memory_map_generation" -value "1" -objects $obj
set_property -name "platform.board_id" -value "ultra96v2" -objects $obj
set_property -name "sim.central_dir" -value "$proj_dir/${_xil_proj_name_}.ip_user_files" -objects $obj
set_property -name "sim.ip.auto_export_scripts" -value "1" -objects $obj
set_property -name "simulator_language" -value "Mixed" -objects $obj

#create the block design by executing the script
source bd.tcl

#create the block design wrapper
make_wrapper -files [get_files $origin_dir/$_xil_proj_name_/$_xil_proj_name_.srcs/sources_1/bd/bd/bd.bd] -top
#add it to the project sources
add_files -norecurse $origin_dir/$_xil_proj_name_/$_xil_proj_name_.gen/sources_1/bd/bd/hdl/bd_wrapper.v
#generates the bitstream
launch_runs impl_1 -to_step write_bitstream -jobs 12
wait_on_run impl_1
#export hw definition file for Vitis
write_hw_platform -fixed -include_bit -force -file $origin_dir/$_xil_proj_name_/bd_wrapper.xsa

