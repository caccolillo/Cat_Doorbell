// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (lin64) Build 3671981 Fri Oct 14 04:59:54 MDT 2022
// Date        : Thu Jul 20 12:56:20 2023
// Host        : caccolillo-OMEN-25L-Desktop-GT12-1xxx running 64-bit Ubuntu 22.04.2 LTS
// Command     : write_verilog -force -mode funcsim
//               /home/caccolillo/Documents/cat_doorbell/Cat_Doorbell/vivado/ultra96_basic_system/ultra96_basic_system.gen/sources_1/bd/bd/ip/bd_blk_mem_gen_0_0/bd_blk_mem_gen_0_0_sim_netlist.v
// Design      : bd_blk_mem_gen_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xczu3eg-sbva484-1-i
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "bd_blk_mem_gen_0_0,blk_mem_gen_v8_4_5,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "blk_mem_gen_v8_4_5,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module bd_blk_mem_gen_0_0
   (clka,
    rsta,
    ena,
    wea,
    addra,
    dina,
    douta,
    clkb,
    rstb,
    enb,
    web,
    addrb,
    dinb,
    doutb,
    rsta_busy,
    rstb_busy);
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME BRAM_PORTA, MEM_SIZE 8192, MEM_WIDTH 32, MEM_ECC NONE, MASTER_TYPE BRAM_CTRL, READ_WRITE_MODE READ_WRITE, READ_LATENCY 1" *) input clka;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA RST" *) input rsta;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA EN" *) input ena;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA WE" *) input [3:0]wea;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA ADDR" *) input [31:0]addra;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA DIN" *) input [31:0]dina;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA DOUT" *) output [31:0]douta;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTB CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME BRAM_PORTB, MEM_SIZE 8192, MEM_WIDTH 32, MEM_ECC NONE, MASTER_TYPE BRAM_CTRL, READ_WRITE_MODE READ_WRITE, READ_LATENCY 1" *) input clkb;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTB RST" *) input rstb;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTB EN" *) input enb;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTB WE" *) input [3:0]web;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTB ADDR" *) input [31:0]addrb;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTB DIN" *) input [31:0]dinb;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTB DOUT" *) output [31:0]doutb;
  output rsta_busy;
  output rstb_busy;

  wire [31:0]addra;
  wire [31:0]addrb;
  wire clka;
  wire clkb;
  wire [31:0]dina;
  wire [31:0]dinb;
  wire [31:0]douta;
  wire [31:0]doutb;
  wire ena;
  wire enb;
  wire rsta;
  wire rsta_busy;
  wire rstb;
  wire rstb_busy;
  wire [3:0]wea;
  wire [3:0]web;
  wire NLW_U0_dbiterr_UNCONNECTED;
  wire NLW_U0_s_axi_arready_UNCONNECTED;
  wire NLW_U0_s_axi_awready_UNCONNECTED;
  wire NLW_U0_s_axi_bvalid_UNCONNECTED;
  wire NLW_U0_s_axi_dbiterr_UNCONNECTED;
  wire NLW_U0_s_axi_rlast_UNCONNECTED;
  wire NLW_U0_s_axi_rvalid_UNCONNECTED;
  wire NLW_U0_s_axi_sbiterr_UNCONNECTED;
  wire NLW_U0_s_axi_wready_UNCONNECTED;
  wire NLW_U0_sbiterr_UNCONNECTED;
  wire [31:0]NLW_U0_rdaddrecc_UNCONNECTED;
  wire [3:0]NLW_U0_s_axi_bid_UNCONNECTED;
  wire [1:0]NLW_U0_s_axi_bresp_UNCONNECTED;
  wire [31:0]NLW_U0_s_axi_rdaddrecc_UNCONNECTED;
  wire [31:0]NLW_U0_s_axi_rdata_UNCONNECTED;
  wire [3:0]NLW_U0_s_axi_rid_UNCONNECTED;
  wire [1:0]NLW_U0_s_axi_rresp_UNCONNECTED;

  (* C_ADDRA_WIDTH = "32" *) 
  (* C_ADDRB_WIDTH = "32" *) 
  (* C_ALGORITHM = "1" *) 
  (* C_AXI_ID_WIDTH = "4" *) 
  (* C_AXI_SLAVE_TYPE = "0" *) 
  (* C_AXI_TYPE = "1" *) 
  (* C_BYTE_SIZE = "8" *) 
  (* C_COMMON_CLK = "0" *) 
  (* C_COUNT_18K_BRAM = "0" *) 
  (* C_COUNT_36K_BRAM = "2" *) 
  (* C_CTRL_ECC_ALGO = "NONE" *) 
  (* C_DEFAULT_DATA = "0" *) 
  (* C_DISABLE_WARN_BHV_COLL = "0" *) 
  (* C_DISABLE_WARN_BHV_RANGE = "0" *) 
  (* C_ELABORATION_DIR = "./" *) 
  (* C_ENABLE_32BIT_ADDRESS = "1" *) 
  (* C_EN_DEEPSLEEP_PIN = "0" *) 
  (* C_EN_ECC_PIPE = "0" *) 
  (* C_EN_RDADDRA_CHG = "0" *) 
  (* C_EN_RDADDRB_CHG = "0" *) 
  (* C_EN_SAFETY_CKT = "1" *) 
  (* C_EN_SHUTDOWN_PIN = "0" *) 
  (* C_EN_SLEEP_PIN = "0" *) 
  (* C_EST_POWER_SUMMARY = "Estimated Power for IP     :     7.734465 mW" *) 
  (* C_FAMILY = "zynquplus" *) 
  (* C_HAS_AXI_ID = "0" *) 
  (* C_HAS_ENA = "1" *) 
  (* C_HAS_ENB = "1" *) 
  (* C_HAS_INJECTERR = "0" *) 
  (* C_HAS_MEM_OUTPUT_REGS_A = "0" *) 
  (* C_HAS_MEM_OUTPUT_REGS_B = "0" *) 
  (* C_HAS_MUX_OUTPUT_REGS_A = "0" *) 
  (* C_HAS_MUX_OUTPUT_REGS_B = "0" *) 
  (* C_HAS_REGCEA = "0" *) 
  (* C_HAS_REGCEB = "0" *) 
  (* C_HAS_RSTA = "1" *) 
  (* C_HAS_RSTB = "1" *) 
  (* C_HAS_SOFTECC_INPUT_REGS_A = "0" *) 
  (* C_HAS_SOFTECC_OUTPUT_REGS_B = "0" *) 
  (* C_INITA_VAL = "0" *) 
  (* C_INITB_VAL = "0" *) 
  (* C_INIT_FILE = "NONE" *) 
  (* C_INIT_FILE_NAME = "no_coe_file_loaded" *) 
  (* C_INTERFACE_TYPE = "0" *) 
  (* C_LOAD_INIT_FILE = "0" *) 
  (* C_MEM_TYPE = "2" *) 
  (* C_MUX_PIPELINE_STAGES = "0" *) 
  (* C_PRIM_TYPE = "1" *) 
  (* C_READ_DEPTH_A = "2048" *) 
  (* C_READ_DEPTH_B = "2048" *) 
  (* C_READ_LATENCY_A = "1" *) 
  (* C_READ_LATENCY_B = "1" *) 
  (* C_READ_WIDTH_A = "32" *) 
  (* C_READ_WIDTH_B = "32" *) 
  (* C_RSTRAM_A = "0" *) 
  (* C_RSTRAM_B = "0" *) 
  (* C_RST_PRIORITY_A = "CE" *) 
  (* C_RST_PRIORITY_B = "CE" *) 
  (* C_SIM_COLLISION_CHECK = "ALL" *) 
  (* C_USE_BRAM_BLOCK = "1" *) 
  (* C_USE_BYTE_WEA = "1" *) 
  (* C_USE_BYTE_WEB = "1" *) 
  (* C_USE_DEFAULT_DATA = "0" *) 
  (* C_USE_ECC = "0" *) 
  (* C_USE_SOFTECC = "0" *) 
  (* C_USE_URAM = "0" *) 
  (* C_WEA_WIDTH = "4" *) 
  (* C_WEB_WIDTH = "4" *) 
  (* C_WRITE_DEPTH_A = "2048" *) 
  (* C_WRITE_DEPTH_B = "2048" *) 
  (* C_WRITE_MODE_A = "WRITE_FIRST" *) 
  (* C_WRITE_MODE_B = "WRITE_FIRST" *) 
  (* C_WRITE_WIDTH_A = "32" *) 
  (* C_WRITE_WIDTH_B = "32" *) 
  (* C_XDEVICEFAMILY = "zynquplus" *) 
  (* downgradeipidentifiedwarnings = "yes" *) 
  (* is_du_within_envelope = "true" *) 
  bd_blk_mem_gen_0_0_blk_mem_gen_v8_4_5 U0
       (.addra({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,addra[12:2],1'b0,1'b0}),
        .addrb({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,addrb[12:2],1'b0,1'b0}),
        .clka(clka),
        .clkb(clkb),
        .dbiterr(NLW_U0_dbiterr_UNCONNECTED),
        .deepsleep(1'b0),
        .dina(dina),
        .dinb(dinb),
        .douta(douta),
        .doutb(doutb),
        .eccpipece(1'b0),
        .ena(ena),
        .enb(enb),
        .injectdbiterr(1'b0),
        .injectsbiterr(1'b0),
        .rdaddrecc(NLW_U0_rdaddrecc_UNCONNECTED[31:0]),
        .regcea(1'b0),
        .regceb(1'b0),
        .rsta(rsta),
        .rsta_busy(rsta_busy),
        .rstb(rstb),
        .rstb_busy(rstb_busy),
        .s_aclk(1'b0),
        .s_aresetn(1'b0),
        .s_axi_araddr({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_arburst({1'b0,1'b0}),
        .s_axi_arid({1'b0,1'b0,1'b0,1'b0}),
        .s_axi_arlen({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_arready(NLW_U0_s_axi_arready_UNCONNECTED),
        .s_axi_arsize({1'b0,1'b0,1'b0}),
        .s_axi_arvalid(1'b0),
        .s_axi_awaddr({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_awburst({1'b0,1'b0}),
        .s_axi_awid({1'b0,1'b0,1'b0,1'b0}),
        .s_axi_awlen({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_awready(NLW_U0_s_axi_awready_UNCONNECTED),
        .s_axi_awsize({1'b0,1'b0,1'b0}),
        .s_axi_awvalid(1'b0),
        .s_axi_bid(NLW_U0_s_axi_bid_UNCONNECTED[3:0]),
        .s_axi_bready(1'b0),
        .s_axi_bresp(NLW_U0_s_axi_bresp_UNCONNECTED[1:0]),
        .s_axi_bvalid(NLW_U0_s_axi_bvalid_UNCONNECTED),
        .s_axi_dbiterr(NLW_U0_s_axi_dbiterr_UNCONNECTED),
        .s_axi_injectdbiterr(1'b0),
        .s_axi_injectsbiterr(1'b0),
        .s_axi_rdaddrecc(NLW_U0_s_axi_rdaddrecc_UNCONNECTED[31:0]),
        .s_axi_rdata(NLW_U0_s_axi_rdata_UNCONNECTED[31:0]),
        .s_axi_rid(NLW_U0_s_axi_rid_UNCONNECTED[3:0]),
        .s_axi_rlast(NLW_U0_s_axi_rlast_UNCONNECTED),
        .s_axi_rready(1'b0),
        .s_axi_rresp(NLW_U0_s_axi_rresp_UNCONNECTED[1:0]),
        .s_axi_rvalid(NLW_U0_s_axi_rvalid_UNCONNECTED),
        .s_axi_sbiterr(NLW_U0_s_axi_sbiterr_UNCONNECTED),
        .s_axi_wdata({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_wlast(1'b0),
        .s_axi_wready(NLW_U0_s_axi_wready_UNCONNECTED),
        .s_axi_wstrb({1'b0,1'b0,1'b0,1'b0}),
        .s_axi_wvalid(1'b0),
        .sbiterr(NLW_U0_sbiterr_UNCONNECTED),
        .shutdown(1'b0),
        .sleep(1'b0),
        .wea(wea),
        .web(web));
endmodule
`pragma protect begin_protected
`pragma protect version = 1
`pragma protect encrypt_agent = "XILINX"
`pragma protect encrypt_agent_info = "Xilinx Encryption Tool 2022.2"
`pragma protect key_keyowner="Synopsys", key_keyname="SNPS-VCS-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
VHPlDkoDlWlBfBMvPBmGYmaek3s9hXXhjF28kllYPnaNm3TSnzzpXHWHc8Ye9/2L2yiQfJ1hTWou
Ia/zeQ8h9/dtr6QB5YkyW4wlb/LbMgXb+DGIXPSllNl0IMsRQIcQDbcQm1bO/nlhb+2pjxiuaQrl
DbvxoDwPs7z3LunRxsg=

`pragma protect key_keyowner="Aldec", key_keyname="ALDEC15_001", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
lmIhoX8hXuc7tNV1sXY1K2/gXL7Y7Hq73qQF7+x03UWWTRd3uhGmVQtOMVbhIW+66UkWUHiD26zL
fzqGor8bgSNGpSFyS11k4TwLQT4OfAMGO8C9Qmmh4+VENBnpS9TW+wHzCv8oUwht7xYtYRZvOvYK
F3fMppz2sBkUd1lciw98ZE/UmNkhqBuMfIYF43j45DEJ55PBhOZNg91Ls4v3qBHyBAaYPFFoMry3
d5Fw1PZyFQSEOSSpwgyds2aN0g6oIwl7zm0LJrM9VDAOxBUE50hk+oHr4jj8J8UhHQJnlEHm1Idm
rvxKygNKRvfSpa90NYxZJFYgqnrMYg+19+9aZA==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VELOCE-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
VkyCjO2onoeZWEoYQ/4ue7X5mkHyTYVW9xjdoTsGS4GdP/Q64VaCZL/jr6R8DVDXPMnH7tRMrDpo
jpYBnyzSgOkfgqM+96ioC2fDyAaG4gYgGLmrBR6qK3/mxXwAZZX+GJ9R/eWXkc9h8xN+gsSSX6/M
jIQCgeT6q7PB4dWT6KY=

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VERIF-SIM-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
Iub91V+TnhVlZCSLu6iKmFjix71y6/l83OPTs8uewWvkE7WcqYxEKi9fonXEkzAtWzuKwEUqnOlN
VBsNJqPUdKcd22q523mrdt89mpdosWD+hvZdO7ELhJniY5u9h49FFkubpN2JiUTcIcKEYxVNlds4
wyvaYUqbPVH5v2ooJwDdimS4GVn9HerCOgPwfshvQDNlMTxLcYju4v8BHMc5Rub9Q/ihvpQU74v2
ouZ9XIwA+C6pBLwvaqS8jE7HXOokgqJilaX/W/t+KEgiFry/txRTMU9WMD7tCN7lcfjCydmS3Lq+
3u6Hsr0S8BwNjcaDpZDnBTygUJd4JSqREnk33w==

`pragma protect key_keyowner="Real Intent", key_keyname="RI-RSA-KEY-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
U46EWFmKmpZGaWfyL+dokyQtJtaOYsa7HCW/+fdtw9/yHKTWFpmqKBZngBj5rPkNhtTDDCJkqsYj
tUXg1j4tgIBaCQn9B0q/aG+B3gPLrudp9hLL25mVbsfiTzdekiV2hJMmhuMoavKKPJHC6zyW7kZi
80er82OQy8h+Df/fe6TRjH9xEt3/b80tRKUMbxkLfnnkAyyf1KfOhB6/uyI4mwXuQR+DsAbzybKR
YtXpOiW72tGrXTFlzcwbHamWZefqsilVpBw6V5dh33vYKGx50xwWpj76maAkpQrOpB7zufeldJe4
W1UOEN84AZdRTLkVSxamWo/wp8nP9fiGS/ItRw==

`pragma protect key_keyowner="Xilinx", key_keyname="xilinxt_2021_07", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
qczgIJYpE/SzErzK7eWJBGcDFEzDLm8cKbwJbPXuM6YnJxx44W+E60R3war7K2QGFAkOoCDUtDC7
SghJGF32btaDLzeKm0tQ669sBtQmMIaBrlt7I9QBkNM8zN9GL92qxNC9o3UVWMOYy5BmH8nUPgcE
O6lRubeltlrTuDe7UJQ2nEPHcXjpUJJ8dxktyW+LovBy1OxW8g4GRAsmEJsoOEg0HuDdWcc4IshJ
PvwPJ7LblELAKsdkSt65y9VaklaEm7MlH4ImlgIa74TgRmutLUbWxM1QYhGE5rAzFhGU5i3RJOdx
L3N7GGGvLMW2z9NSHbIFX+/eNII9fNJ9nZbgLA==

`pragma protect key_keyowner="Metrics Technologies Inc.", key_keyname="DSim", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
Ti1NUgDv8YPk90APMwfu/mRr38QYwAxZfv0T6zQ89YS55t2EquEGVqrEafYX6rTydLOw8le1Oucv
f2oERpSSSTih/ScZneSZmuPE/Zh2BU1Ajv0j+/+0uEWXU+5lLPbDJjnapTmJXih1MYPf0SHpZZmE
BKj2IEBI9MPZlh6bxpa5BWJnyPdAvHf+UNaMXU9+pmbtrzUVebql4mFJu45Z3+ehmFY4FBW3zXMF
44C4TlHACLwL3vHVMCVfeKhgdVDbpE+/IFhTStz7mZ9h9RKGanQcs6YDVM1R+2RKA1QT1fX4FiQc
1V+FGmrm1ujxmFGXwpfNKByVlfCY0oWhRJCYYQ==

`pragma protect key_keyowner="Atrenta", key_keyname="ATR-SG-RSA-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=384)
`pragma protect key_block
HuEXFK0NXt09xU2yxxjng1OLsT+ZEM4EhqBgpr9D2ljw2vDaMBrqEsRQTc2B9soDq3ewDduHJXBd
OGYxkPnoN6LhjULtB2nTgjcH6NxA4puZ1ZNcndDndVBo8rTW5W1OqHq6InAG0CqPpTIkuqz3ECPl
EysI++MCDfH6tIzlekxJFIJ1McJsTq5rFuLzMMcrmkBxgcayDpOcCFuzZzCczxmt/cCCIKmDybwT
OQXmOcLJoYLP4sFu6R9c6xO8i6p++crv2N3eIxZHKbek9xBBZqQM9EYuEtsbkqAs9XZpa16i5njR
BDFxTKcP6r7JgFALJE89AZhBbate5JXWp0v4ECZD18aEL17CipwcWPutNMdG1apzSPP5y59n7rMG
yxBPz1gKHc3Emkl4WcO0hjICxqmO6dMXoY8JvBSf6ry2l0sH9Ihr3Bq5WWmlhPHnoaNr5jl//vNe
KfToWtn97eoVSt1LnmXXnSpdigbHr0UIg8AdkpdkuNRaWdVicDdgSo49

`pragma protect key_keyowner="Cadence Design Systems.", key_keyname="CDS_RSA_KEY_VER_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
mokwst2bn6UxD6V9UdIgCIG1QQ/d0FiJqYGOTI2eHPV6YElaLjnJ8DnQmZnGS95o3x93FDOoa58C
RwYsX1fVoVtXkj1LuZq0k7q9vEe4T8xMjpkeYtIHY9k0Xhy1Lq/xRlfzGAf9fvf9e+f4r7aR/Sb/
uCZxxugG5niTwLENY1n3NthYL0jvo8Fmdw4Qg0nTCGWlVCws+09K0g9/lx6I9EcuHHemcHO3fOZG
lMc4NaPNozKwnyDMoWUkwiVxyFEPFaQLNYqzjvR+CqrWfhFLo96JWhL+eaDoNuZoBVYQtNH5ZwBL
BoO27Pw10lgcReGlZBz3BLO7T4ddynCx0+eSnw==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
PiP7AjOQqqouyQMoBQqgWIDhUSViq94rIvGiIJ/UKMDspM/yXw1caE8AhWHTjYckC4yLpPAz5P6s
1Z6flzDPrzVwg4e59X2cc4IMCHhedna0rDO804njcc6amRDTeLsMLTkWfvomB4xwszm2AgT+PRnB
WHd09ZUDVFjiBXT+Oa9AicgGJHrX3w823yBPuAa704kje/SzgtiDpcTU1eLmLhLW7LpEd9KIHd9s
ER7Uk9Orws0Kq9PMTqMX4hMn5K5mFakOeOURiEbUjdv5RiIJ2g/PlQXSItM8fHsBTQa6fOaJwQTI
vHwK3a8ZBHpfT1YH+n7wNiNUZwD4SFXm1QVx4g==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-PREC-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
Ul5ZfTHJwMctaNhYRortUZizYMPYRef7uYqPSuMkxsArnxI/cjGh+KRMwzV86hyp/6TXSJIjm5ec
2wX2UONdPN+DOJ84jYC4JbgJQrPnTj7ioD8uLX/WlyPcQzyF5keqFgj5eR5s13FskVWCuAWf5m9w
mhFEKFjVXDAr7gVgAJh/hL8P6Psrnf+LGfiM8JhnDepsHEYykGlpD3fzru2BGgqHWqPqFMcnyVGl
vysaIXiJz/eYKvO8RGcgd3DJAM/wPm9A0m/DWcmSnczOgTjoqkHcBg2H5uJMLvufzmjImi6LYEqq
v04ESDEN31cSUzqUYcayvMFOnI/WNsWbFIa5+Q==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 64384)
`pragma protect data_block
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
`pragma protect end_protected
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;
    parameter GRES_WIDTH = 10000;
    parameter GRES_START = 10000;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
    wire GRESTORE;
    tri1 p_up_tmp;
    tri (weak1, strong0) PLL_LOCKG = p_up_tmp;

    wire PROGB_GLBL;
    wire CCLKO_GLBL;
    wire FCSBO_GLBL;
    wire [3:0] DO_GLBL;
    wire [3:0] DI_GLBL;
   
    reg GSR_int;
    reg GTS_int;
    reg PRLD_int;
    reg GRESTORE_int;

//--------   JTAG Globals --------------
    wire JTAG_TDO_GLBL;
    wire JTAG_TCK_GLBL;
    wire JTAG_TDI_GLBL;
    wire JTAG_TMS_GLBL;
    wire JTAG_TRST_GLBL;

    reg JTAG_CAPTURE_GLBL;
    reg JTAG_RESET_GLBL;
    reg JTAG_SHIFT_GLBL;
    reg JTAG_UPDATE_GLBL;
    reg JTAG_RUNTEST_GLBL;

    reg JTAG_SEL1_GLBL = 0;
    reg JTAG_SEL2_GLBL = 0 ;
    reg JTAG_SEL3_GLBL = 0;
    reg JTAG_SEL4_GLBL = 0;

    reg JTAG_USER_TDO1_GLBL = 1'bz;
    reg JTAG_USER_TDO2_GLBL = 1'bz;
    reg JTAG_USER_TDO3_GLBL = 1'bz;
    reg JTAG_USER_TDO4_GLBL = 1'bz;

    assign (strong1, weak0) GSR = GSR_int;
    assign (strong1, weak0) GTS = GTS_int;
    assign (weak1, weak0) PRLD = PRLD_int;
    assign (strong1, weak0) GRESTORE = GRESTORE_int;

    initial begin
	GSR_int = 1'b1;
	PRLD_int = 1'b1;
	#(ROC_WIDTH)
	GSR_int = 1'b0;
	PRLD_int = 1'b0;
    end

    initial begin
	GTS_int = 1'b1;
	#(TOC_WIDTH)
	GTS_int = 1'b0;
    end

    initial begin 
	GRESTORE_int = 1'b0;
	#(GRES_START);
	GRESTORE_int = 1'b1;
	#(GRES_WIDTH);
	GRESTORE_int = 1'b0;
    end

endmodule
`endif
