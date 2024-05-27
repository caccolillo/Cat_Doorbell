// control
// 0x00 : Control signals
//        bit 0  - ap_start (Read/Write/COH)
//        bit 1  - ap_done (Read)
//        bit 2  - ap_idle (Read)
//        bit 3  - ap_ready (Read/COR)
//        bit 4  - ap_continue (Read/Write/SC)
//        bit 7  - auto_restart (Read/Write)
//        bit 9  - interrupt (Read)
//        others - reserved
// 0x04 : Global Interrupt Enable Register
//        bit 0  - Global Interrupt Enable (Read/Write)
//        others - reserved
// 0x08 : IP Interrupt Enable Register (Read/Write)
//        bit 0 - enable ap_done interrupt (Read/Write)
//        bit 1 - enable ap_ready interrupt (Read/Write)
//        others - reserved
// 0x0c : IP Interrupt Status Register (Read/TOW)
//        bit 0 - ap_done (Read/TOW)
//        bit 1 - ap_ready (Read/TOW)
//        others - reserved
// 0x10 : Data signal of in1
//        bit 31~0 - in1[31:0] (Read/Write)
// 0x14 : Data signal of in1
//        bit 31~0 - in1[63:32] (Read/Write)
// 0x18 : reserved
// 0x1c : Data signal of in2
//        bit 31~0 - in2[31:0] (Read/Write)
// 0x20 : Data signal of in2
//        bit 31~0 - in2[63:32] (Read/Write)
// 0x24 : reserved
// 0x28 : Data signal of out_r
//        bit 31~0 - out_r[31:0] (Read/Write)
// 0x2c : Data signal of out_r
//        bit 31~0 - out_r[63:32] (Read/Write)
// 0x30 : reserved
// 0x34 : Data signal of scale_by_4
//        bit 31~0 - scale_by_4[31:0] (Read/Write)
// 0x38 : reserved
// 0x3c : Data signal of size
//        bit 31~0 - size[31:0] (Read/Write)
// 0x40 : reserved
// (SC = Self Clear, COR = Clear on Read, TOW = Toggle on Write, COH = Clear on Handshake)

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <linux/types.h>

#define XKRNL_IMG_AVERAGING_BASE_ADDRESS		         0xa0000000
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_AP_CTRL         0x00
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_GIE             0x04
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_IER             0x08
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_ISR             0x0c
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN1_DATA        0x10
#define XKRNL_IMG_AVERAGING_CONTROL_BITS_IN1_DATA        64
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN2_DATA        0x1c
#define XKRNL_IMG_AVERAGING_CONTROL_BITS_IN2_DATA        64
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_OUT_R_DATA      0x28
#define XKRNL_IMG_AVERAGING_CONTROL_BITS_OUT_R_DATA      64
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_SCALE_BY_4_DATA 0x34
#define XKRNL_IMG_AVERAGING_CONTROL_BITS_SCALE_BY_4_DATA 32
#define XKRNL_IMG_AVERAGING_CONTROL_ADDR_SIZE_DATA       0x3c
#define XKRNL_IMG_AVERAGING_CONTROL_BITS_SIZE_DATA       32

#define MAP_SIZE 4096UL
#define MAP_MASK (MAP_SIZE - 1)
#define IMAGE_SIZE 921600

void start_core(void *mapped_dev_base){  //start the kernel
	*((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_AP_CTRL)) = 1;
}

//void set_addr_inp1(void *mapped_dev_base, __u64 addr){ //set the starting address for input 1
//  __u32 data;
//
//  //write the low part of the 64 bits address
//  data = (__u32)(addr & 0x00000000ffffffff);
//  *((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN1_DATA)) = data;
//
//  //write the high part of the 64 bits address
//  data = (__u32)((addr & 0xffffffff00000000)>>32);
//  *((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN1_DATA + 4)) = data;
//}

void set_addr_inp1(void *mapped_dev_base, __u64 addr){ //set the starting address for input 1
  *((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN1_DATA)) = addr;
}

void set_addr_inp2(void *mapped_dev_base, __u64 addr){ //set the starting address for input 2
//  *((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN2_DATA)) = addr;
//  *((__u64 *)(mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN2_DATA)) = addr;
}

void set_addr_out(void *mapped_dev_base, __u64 addr){  //set the destination address for output
  *((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_OUT_R_DATA)) = addr;
}

void set_size(void *mapped_dev_base, int img_size){  //set the size of the image to process
  *((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_SIZE_DATA)) = img_size;
}

void manage_scale_by_4(void *mapped_dev_base, int scale_flag){ //enables/disables the scaling of the result by 4
  *((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_SCALE_BY_4_DATA)) = scale_flag;
}

int is_done(void *mapped_dev_base){ //returns the status of the done flag
  int ap_ctrl = 0;

  ap_ctrl = *((unsigned long *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_AP_CTRL));
  return (ap_ctrl >> 1) & 0x1;
}

void run_img_averaging(void *mapped_dev_base, int img_size, int scale_flag, __u64 addr_inp1, __u64 addr_inp2, __u64 addr_out){ //run a single iteration of the img_averaging kernel
  set_addr_inp1(mapped_dev_base, addr_inp1); //set the starting address for input 1
  //set_addr_inp2(mapped_dev_base, addr_inp2); //set the starting address for input 2
  set_addr_out(mapped_dev_base, addr_out);  //set the destination address for output
  set_size(mapped_dev_base, img_size);  //set the size of the image to process
  manage_scale_by_4(mapped_dev_base, scale_flag); //enables/disables the scaling of the result by 4
  start_core(mapped_dev_base);  //start the kernel
  while (!is_done(mapped_dev_base)); //returns the status of the done flag
}

int main(){

	int memfd;
	void *mapped_base, *mapped_dev_base;
	off_t dev_base = XKRNL_IMG_AVERAGING_BASE_ADDRESS;

	__u64 addr_inp1; //starting address input image 1
	__u64 addr_inp2; //starting address input image 2
	__u64 addr_out;  //destination address output image
	int img_size = IMAGE_SIZE; //specifies the image size in pixels
    int scale_flag; //0 = no scaling by 4, 1 = scaling by 4

    printf("Image averaging '' DRIVER '' \n");

	//***********************************************************************
    //Allocate memory buffers for input - output images
    //***********************************************************************
    addr_inp1 = malloc (sizeof (int)*img_size);

    addr_inp2 = malloc (sizeof (int)*img_size);

    addr_out = malloc (sizeof (int)*img_size);

	//***********************************************************************
    //Open "/dev/mem"
    //***********************************************************************

	memfd = open("/dev/mem", O_RDWR | O_SYNC);
    	if (memfd == -1) {
		printf("Can't open /dev/mem.\n");
		exit(0);
	}
	printf("/dev/mem opened.\n");

	//***********************************************************************
	// Map one page of memory into user space such that the device is in that
	// page, but it may not be at the start of the page
	//***********************************************************************

	mapped_base = mmap(0, MAP_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, memfd, dev_base & ~MAP_MASK);
    	if (mapped_base == (void *) -1) {
		printf("Can't map the memory to user space.\n");
		exit(0);
	}
 	printf("Memory mapped at address %x \n", mapped_base);

	//***************************************************************************
	// get the address of the device in user space which will be an offset
 	// from the base that was mapped as memory is mapped at the start of a page
	//***************************************************************************

	mapped_dev_base = mapped_base + (dev_base & MAP_MASK);

	//***********************************************************************
    //Manage the img_averaging HLS kernel
	//***********************************************************************
 	printf("Running kernel \n", mapped_base);
	run_img_averaging(mapped_dev_base, img_size, scale_flag, addr_inp1, addr_inp2, addr_out); //run a single iteration of the img_averaging kernel
 	printf("Kernel done \n", mapped_base);

	//***********************************************************************
	// unmap the memory before exiting
	//***********************************************************************

	if (munmap(mapped_base, MAP_SIZE) == -1) {
		printf("Can't unmap memory from user space.\n");
		exit(0);
	}

	close(memfd);
    return 0;
}
