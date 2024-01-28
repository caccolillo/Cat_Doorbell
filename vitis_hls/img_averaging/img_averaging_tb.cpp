//#include "img_averaging.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define DATA_SIZE 921600

extern "C" void krnl_img_averaging(uint32_t* in1, uint32_t* in2, uint32_t* out, int scale_by_4, int size);


//loads the matrix with the content loaded from the file
//returns -1 in case or error, othervise it gives back the number of elements read from file and loaded in the matrix
int load_data(const char *filename, uint32_t *frame){
  int loop = 0; //loop counter
  ssize_t nbytes; //number of characters hold in the line read from the input file
  string line; //this will contain the data read from the file
  //loads the arrays with the file contents

  ifstream myfile (filename); //opening the file.
  if(myfile.is_open()){ //if the file is open
	while (!myfile.eof()){ //while the end of file is NOT reached
	  getline (myfile,line); //get one line from the file
	  nbytes = line.length();
	  if(nbytes){
		frame[loop] = stoi(line);
		//cout << frame[loop] << " ---  "<< nbytes << endl; //and output it
		loop++;
	  }
	}
	myfile.close(); //closing the file
	cout << "File " << filename << " finished, closing it." << endl;
	return loop;
  }
  else cout << "Unable to open file" << endl; //if the file is not open output
  return -1;
}


//compares the content of two arrays, giving back the number of different elements
int cmp_results(uint32_t *avg_frame, uint32_t *golden_ref, int size){
  int numerr = 0;
  for (int i = 0; i < size; i++) {
	if(avg_frame[i] != golden_ref[i]){
	  ++numerr;
	}
  }
  return numerr;
}

//main program
int main(void){
  //allocate array for frame 1, 2, 3, 4 and average frame
  uint32_t *frame1 = new uint32_t[DATA_SIZE];
  uint32_t *frame2 = new uint32_t[DATA_SIZE];
  uint32_t *frame3 = new uint32_t[DATA_SIZE];
  uint32_t *frame4 = new uint32_t[DATA_SIZE];
  uint32_t *avg_frm = new uint32_t[DATA_SIZE];
  uint32_t *tmp1 = new uint32_t[DATA_SIZE];
  uint32_t *tmp = new uint32_t[DATA_SIZE];
  uint32_t *avg = new uint32_t[DATA_SIZE];


  int loop = 0; //number of pixels processed
  int numerrors = 0; //number of different pixels from the golden reference
  ssize_t nbytes;
  string line; //this will contain the data read from the file



  //loads the arrays with the file contents
  loop =  load_data("frame1.txt", frame1); //load frame 1
  loop =  load_data("frame2.txt", frame2); //load frame 2
  loop =  load_data("frame3.txt", frame3); //load frame 3
  loop =  load_data("frame4.txt", frame4); //load frame 4
  loop =  load_data("average_frame.txt", avg_frm); //load the golden reference average frame



  //invokes the UUT
  krnl_img_averaging(&frame1[0], &frame2[0], &tmp[0], 0, loop);
  krnl_img_averaging(&frame3[0], &frame4[0], &tmp1[0], 0, loop);
  krnl_img_averaging(&tmp[0], &tmp1[0], &avg[0], 1, loop);
  //checks the computed output against the golden reference
  numerrors =  cmp_results(&avg_frm[0], &avg[0], loop);

  //decides if the execution has been successful or not
  if(numerrors){
	cout << "Found " << numerrors << " errors, test failed!" << endl;
  }
  else{
	cout << "No errors found, test passed!" << endl;
  }
  //testbench ended
  return numerrors;
}

