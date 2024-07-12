# This file contains a function that can be called from a bd
# tcl file from Vivado to add the acceleration platform related
# tcl attributes. There is a lot of hard coding in here, but
# keeping it separate makes it easier to change the Vivado hardware
# design.
#
# Add this to the bottom of the exported bd tcl:
# source $::env(PWS)/bin/accel-platform.tcl
# accel-platform

proc accel-platform {} {

    # Begin Accel Platform Stuff
    set pws           "./"
    set proj          "./myproj"
    set pfm_dir       "./"
    set xsa_file_name "u9sv2.xsa"
    set board_id      "ultra96v2"
    set bd_file       "myproj/project_1.srcs/sources_1/bd/design_1/design_1.bd"
    set wrapper_file  "myproj/project_1.srcs/sources_1/bd/design_1/hdl/design_1_wrapper.v"
    set dynamic_postlink_file "${pws}/bin/dynamic_postlink.tcl"
    set maxThreads    4

    set_param general.maxThreads ${maxThreads}

    # Enable platform interfaces
    set_property PFM_NAME "avnet:${board_id}:${proj}:1.0" \
	[get_files ${bd_file}]

    # Mark interfaces for accel use
    # Currently already done above, but would like to do programmatically
    # down here, later
    #set_property PFM.CLOCK
    #{
    # clk_out1 { id "1" is_default "false" proc_sys_reset "/proc_sys_reset_0" status "fixed"}
    # clk_out2 { id "2" is_default "false" proc_sys_reset "/proc_sys_reset_1" status "fixed"}
    # clk_out3 { id "0" is_default "true"  proc_sys_reset "/proc_sys_reset_2" status "fixed"}
    # clk_out4 { id "4" is_default "false" proc_sys_reset "/proc_sys_reset_3" status "fixed"}
    # clk_out5 { id "5" is_default "false" proc_sys_reset "/proc_sys_reset_4" status "fixed"}
    #} [get_bd_cells /clk_wiz_0]

    #set_property PFM.AXI_PORT
    #{
    # M_AXI_HPM0_FPD {memport "M_AXI_GP"  sptag "" memory ""}
    # M_AXI_HPM1_FPD {memport "M_AXI_GP"  sptag "" memory ""}
    # S_AXI_HPC0_FPD {memport "S_AXI_HPC" sptag "" memory ""}
    # S_AXI_HPC1_FPD {memport "S_AXI_HPC" sptag "" memory ""}
    # S_AXI_HP0_FPD  {memport "S_AXI_HP"  sptag "" memory ""}
    # S_AXI_HP1_FPD  {memport "S_AXI_HP"  sptag "" memory ""}
    # S_AXI_HP2_FPD  {memport "S_AXI_HP"  sptag "" memory ""}
    # S_AXI_HP3_FPD  {memport "S_AXI_HP"  sptag "" memory ""}
    #} [get_bd_cells /zynq_ultra_ps_e_0]


    # UG1393 CH52
    set_property platform.design_intent.embedded true        [current_project]
    set_property platform.design_intent.server_managed false [current_project]
    set_property platform.design_intent.external_host false  [current_project]
    set_property platform.design_intent.datacenter false     [current_project]
    set_property platform.default_output_type "sd_card"      [current_project]
    set_property platform.post_sys_link_tcl_hook ${dynamic_postlink_file} [current_project]

    regenerate_bd_layout
    validate_bd_design -force
    save_bd_design

    # Trying to do this programmatically so that I can add arbitrary IP
    # later, and still have this portion of the script work
    set l_ips [get_ips -all]
    foreach ip $l_ips {
	catch { config_ip_cache -export $ip }
    }

    export_ip_user_files -of_objects                                      \
	[get_files ${bd_file}] \
	-no_script -sync -force -quiet

    create_ip_run [get_files -of_objects [get_fileset sources_1]          \
		       ${bd_file}]

    # Apparently, there is no lmap function in Vivado's Tcl...shame
    # Generate a list with members representing strings to match synth jobs
    foreach a $l_ips { lappend l_ips_synth [append a "_synth_1"] }

    launch_runs -jobs ${maxThreads} $l_ips_synth

    # Try to just wait on the last run, appears to work
    wait_on_run [lindex $l_ips_synth end]

    # Create the HDL wrapper top level
    make_wrapper -files [get_files ${bd_file}] -top
    add_files -norecurse ${wrapper_file}

    launch_runs synth_1 -jobs ${maxThreads}
    wait_on_run synth_1

    launch_runs impl_1 -to_step write_bitstream -jobs ${maxThreads}
    wait_on_run impl_1

    write_hw_platform    -include_bit -force ${pfm_dir}/${xsa_file_name}
    validate_hw_platform -verbose            ${pfm_dir}/${xsa_file_name}

}
