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

#define IN1_BUF_ADDR 0x0d000000
#define IN2_BUF_ADDR 0x0e000000
#define OUT_BUF_ADDR 0x0f000000


//loads the matrix with the content loaded from the file
//returns -1 in case or error, otherwise it gives back the number of elements read from file and loaded in the matrix
int load_data(const char *filename, __u32 *frame){
  int count = 0;

  FILE *fp = fopen(filename, "r"); //open the file in read mode
  if (fp == NULL){
    printf("Error: could not open file %s", filename);
    return 1;
  }

  while(!feof(fp)){  //loop until the end of the file
    fscanf(fp, "%d", &frame[count]); //read a row and interpret as an integer, store it in the file
    count++;
  }

  fclose(fp);
  return count;
}

//saves on a file the content of the matrix
//returns -1 in case or error, otherwise it gives back the number of elements read from file and loaded in the matrix
int save_data(const char *filename, __u32 *frame, __u32 numpixels){
  int count = 0;

  FILE *fp = fopen(filename, "w"); //open the file in write mode
  if (fp == NULL){
    printf("Error: could not open file %s", filename);
    return 1;
  }

  while(count < numpixels){  //loop until the end of the pixels
    fprintf(fp, "%d \n", frame[count]); //store a pixel in the file
    count++;
  }

  fclose(fp);
  return count;
}


void start_core(void *mapped_dev_base){  //start the kernel
	*((__u32 *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_AP_CTRL)) = 1;
}

void set_addr_inp1(void *mapped_dev_base, __u32 addr){ //set the starting address for input 1
  *((__u32 *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN1_DATA)) = addr;
}

void set_addr_inp2(void *mapped_dev_base, __u32 addr){ //set the starting address for input 2
  *((__u32 *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_IN2_DATA)) = addr;
}

void set_addr_out(void *mapped_dev_base, __u32 addr){  //set the destination address for output
  *((__u32 *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_OUT_R_DATA)) = addr;
}

void set_size(void *mapped_dev_base, int img_size){  //set the size of the image to process
  *((__u32 *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_SIZE_DATA)) = img_size;
}

void manage_scale_by_4(void *mapped_dev_base, int scale_flag){ //enables/disables the scaling of the result by 4
  *((__u32 *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_SCALE_BY_4_DATA)) = scale_flag;
}

int is_done(void *mapped_dev_base){ //returns the status of the done flag
  int ap_ctrl = 0;

  ap_ctrl = *((__u32 *) (mapped_dev_base + XKRNL_IMG_AVERAGING_CONTROL_ADDR_AP_CTRL));
  return (ap_ctrl >> 1) & 0x1;
}

void run_img_averaging(void *mapped_dev_base, int img_size, int scale_flag, __u32 addr_inp1, __u32 addr_inp2, __u32 addr_out){ //run a single iteration of the img_averaging kernel
  printf("Setting source address input image 1 \n");
  set_addr_inp1(mapped_dev_base, addr_inp1); //set the starting address for input 1
  printf("Setting destination address input image 2 \n");
  set_addr_inp2(mapped_dev_base, addr_inp2); //set the starting address for input 2
  printf("Setting destination address output image \n");
  set_addr_out(mapped_dev_base, addr_out);  //set the destination address for output
  printf("Setting input images size \n");
  set_size(mapped_dev_base, img_size);  //set the size of the image to process
  printf("Managing scale by four flag \n");
  manage_scale_by_4(mapped_dev_base, scale_flag); //enables/disables the scaling of the result by 4
  printf("Starting the kernel \n");
  start_core(mapped_dev_base);  //start the kernel
  while (!is_done(mapped_dev_base)); //returns the status of the done flag
  printf("Kernel done \n");
}

int main(){

	int memfd;
	int num_pixels_loaded;
	void *mapped_base, *mapped_dev_base;
	off_t dev_base = XKRNL_IMG_AVERAGING_BASE_ADDRESS;

	__u32 addr_inp1; //starting address input image 1
	__u32 addr_inp2; //starting address input image 2
	__u32 addr_out;  //destination address output image
	int img_size = IMAGE_SIZE; //specifies the image size in pixels
    int scale_flag; //0 = no scaling by 4, 1 = scaling by 4
	__u32 *inp1_array; //pointer to the array holding inp1
	__u32 *inp2_array; //pointer to the array holding inp2
	__u32 *out_array; //pointer to the array holding out


    printf("Image averaging '' DRIVER '' \n");

	//***********************************************************************
    //Allocate three memory buffers for inp1, inp2 and out
    //***********************************************************************
    inp1_array = (int*) malloc(IMAGE_SIZE * sizeof(int));
    if (inp1_array == NULL) {
        printf("Memory allocation failed for inp1_array!");
		exit(0);
    }

    inp2_array = (int*) malloc(IMAGE_SIZE * sizeof(int));
    if (inp2_array == NULL) {
        printf("Memory allocation failed for inp2_array!");
		exit(0);
    }

    out_array = (int*) malloc(IMAGE_SIZE * sizeof(int));
    if (out_array == NULL) {
        printf("Memory allocation failed for out_array!");
		exit(0);
    }

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

	mapped_base = mmap(0, 65535, PROT_READ | PROT_WRITE, MAP_SHARED, memfd, dev_base);
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
    //Allocate memory buffers for input - output images
    //***********************************************************************

    addr_inp1 = mmap(0, (sizeof (int)*img_size), PROT_READ | PROT_WRITE, MAP_SHARED, memfd, IN1_BUF_ADDR);
	if (addr_inp1 == (void *) -1) {
	  printf("Can't map the memory ''IN1_BUF_ADDR'' to user space.\n");
	  exit(0);
    }
	printf("Memory ''IN1_BUF_ADDR'' mapped at address %x \n", addr_inp1);

    addr_inp2 = mmap(0, (sizeof (int)*img_size), PROT_READ | PROT_WRITE, MAP_SHARED, memfd, IN2_BUF_ADDR);
	if (addr_inp2 == (void *) -1) {
	  printf("Can't map the memory ''IN2_BUF_ADDR'' to user space.\n");
	  exit(0);
    }
	printf("Memory ''IN2_BUF_ADDR'' mapped at address %x \n", addr_inp2);

	addr_out = mmap(0, (sizeof (int)*img_size), PROT_READ | PROT_WRITE, MAP_SHARED, memfd, OUT_BUF_ADDR);
	if (addr_out == (void *) -1) {
	  printf("Can't map the memory ''OUT_BUF_ADDR'' to user space.\n");
	  exit(0);
    }
	printf("Memory ''OUT_BUF_ADDR'' mapped at address %x \n", addr_out);

	//***********************************************************************
    //Initialize memory buffers for inp1 and inp2 with files content
    //***********************************************************************
	num_pixels_loaded =  load_data("frame1.txt", (__u32 *)(addr_inp1));
    if(num_pixels_loaded != IMAGE_SIZE){
  	  printf("Can't initialize ''IN1_BUF'' with ''frame1.txt''.\n");
  	  exit(0);
    }

	num_pixels_loaded =  load_data("frame2.txt", (__u32 *)(addr_inp2));
    if(num_pixels_loaded != IMAGE_SIZE){
  	  printf("Can't initialize ''IN2_BUF'' with ''frame2.txt''.\n");
  	  exit(0);
    }

	//***********************************************************************
    //Manage the img_averaging HLS kernel for the first run
	//***********************************************************************
 	printf("Running kernel on ''frame1.txt'' and ''frame2.txt''\n", mapped_base);
	run_img_averaging(mapped_dev_base, img_size, scale_flag, addr_inp1, addr_inp2, addr_out); //run a single iteration of the img_averaging kernel
 	printf("Kernel done, produced output1 \n", mapped_base);

	//***********************************************************************
    //Initialize memory buffer for inp1 with files content
    //***********************************************************************
	num_pixels_loaded =  load_data("frame3.txt", (__u32 *)(addr_inp1));
    if(num_pixels_loaded != IMAGE_SIZE){
  	  printf("Can't initialize ''IN1_BUF'' with ''frame1.txt''.\n");
  	  exit(0);
    }

	//***********************************************************************
    //Manage the img_averaging HLS kernel for the second run
	//***********************************************************************
 	printf("Running kernel on ''frame3.txt'' and output1 \n", mapped_base);
	run_img_averaging(mapped_dev_base, img_size, scale_flag, addr_inp1, addr_out, addr_inp2); //run a single iteration of the img_averaging kernel
 	printf("Kernel done, produced output2 \n", mapped_base);

	//***********************************************************************
    //Initialize memory buffer for inp2 with files content
    //***********************************************************************
	num_pixels_loaded =  load_data("frame4.txt", (__u32 *)(addr_inp1));
    if(num_pixels_loaded != IMAGE_SIZE){
  	  printf("Can't initialize ''IN1_BUF'' with ''frame4.txt''.\n");
  	  exit(0);
    }

	//***********************************************************************
    //Manage the img_averaging HLS kernel for the second run
	//***********************************************************************
 	printf("Running kernel on ''frame3.txt'' and output1 \n", mapped_base);
 	scale_flag = 1; //introduce scaling by 4
	run_img_averaging(mapped_dev_base, img_size, scale_flag, addr_inp1, addr_inp2, addr_out); //run a single iteration of the img_averaging kernel
 	printf("Kernel done, produced output4 \n", mapped_base);

	//***********************************************************************
    //save the final output image
	//***********************************************************************
	num_pixels_loaded =  save_data("outputframe.txt", (__u32 *)(addr_out), IMAGE_SIZE);
    if(num_pixels_loaded != IMAGE_SIZE){
  	  printf("Can't create ''outputframe.txt''.\n");
  	  exit(0);
    }
	//***********************************************************************
	// unmap the memory before exiting
	//***********************************************************************

	if (munmap(mapped_base, MAP_SIZE) == -1) {
		printf("Can't unmap memory from user space.\n");
		exit(0);
	}

	close(memfd);

 	printf("Exiting \n", mapped_base);
    return 0;
}
