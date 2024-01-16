//#include "img_averaging.h"

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define DATA_SIZE 921600

extern 	void krnl_img_averaging(uint32_t* in1, uint32_t* in2, uint32_t* out, int scale_by_4, int size);

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


  int loop = 0; //loop counter
  string line; //this will contain the data read from the file



  //loads the arrays with the file contents

  //load frame1
  loop = 0;
  ifstream myfile ("frame1.txt"); //opening the file.
  if (myfile.is_open()) //if the file is open
  {
      while (! myfile.eof() ) //while the end of file is NOT reached
      {
          getline (myfile,line); //get one line from the file
          frame1[loop] = stoi(line);
          cout << frame1[loop] << endl; //and output it
          loop++;
      }
      myfile.close(); //closing the file
  }
  else cout << "Unable to open file"; //if the file is not open output

  //load frame2
  loop = 0;
  ifstream myfile1 ("frame2.txt"); //opening the file.
  if (myfile1.is_open()) //if the file is open
  {
      while (! myfile.eof() ) //while the end of file is NOT reached
      {
          getline (myfile1,line); //get one line from the file
          frame2[loop] = stoi(line);
          cout << frame2[loop] << endl; //and output it
          loop++;
      }
      myfile1.close(); //closing the file
  }
  else cout << "Unable to open file"; //if the file is not open output


  //load frame3
  loop = 0;
  ifstream myfile2 ("frame3.txt"); //opening the file.
  if (myfile2.is_open()) //if the file is open
  {
      while (! myfile2.eof() ) //while the end of file is NOT reached
      {
          getline (myfile2,line); //get one line from the file
          frame3[loop] = stoi(line);
          cout << frame3[loop] << endl; //and output it
          loop++;
      }
      myfile2.close(); //closing the file
  }
  else cout << "Unable to open file"; //if the file is not open output

  //load frame4
  loop = 0;
  ifstream myfile3 ("frame4.txt"); //opening the file.
  if (myfile3.is_open()) //if the file is open
  {
      while (! myfile3.eof() ) //while the end of file is NOT reached
      {
          getline (myfile3,line); //get one line from the file
          frame4[loop] = stoi(line);
          cout << frame4[loop] << endl; //and output it
          loop++;
      }
      myfile3.close(); //closing the file
  }
  else cout << "Unable to open file"; //if the file is not open output

  //load avg_frm
  loop = 0;
  ifstream myfile4 ("average_frame.txt"); //opening the file.
  if (myfile4.is_open()) //if the file is open
  {
      while (! myfile4.eof() ) //while the end of file is NOT reached
      {
          getline (myfile4,line); //get one line from the file
          avg_frm[loop] = stoi(line);
          cout << avg_frm[loop] << endl; //and output it
          loop++;
      }
      myfile4.close(); //closing the file
  }
  else cout << "Unable to open file"; //if the file is not open output


  system("PAUSE");
  return 0;

  //invokes the UUT
  krnl_img_averaging(&frame1[0], &frame2[0], &tmp[0], 0, loop);
  krnl_img_averaging(&frame3[0], &frame4[0], &tmp1[0], 0, loop);
  krnl_img_averaging(&tmp[0], &tmp1[0], &avg[0], 1, loop);
  //checks the computed output against the golden reference

  //decides if the execution has been successful or not

}

