//#include "img_averaging.h"

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define DATA_SIZE 921600



//main program
int main(void){
  //allocate array for frame 1, 2, 3, 4 and average frame
  uint32_t *frame1 = new uint32_t[DATA_SIZE];
  uint32_t *frame2 = new uint32_t[DATA_SIZE];
  uint32_t *frame3 = new uint32_t[DATA_SIZE];
  uint32_t *frame4 = new uint32_t[DATA_SIZE];
  uint32_t *avg_frm = new uint32_t[DATA_SIZE];

  //loads the arrays with the file contents
  int loop = 0; //short for loop for input
  string line; //this will contain the data read from the file
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

  system("PAUSE");
  return 0;





  //invokes the UUT

  //checks the computed output against the golden reference

  //decides if the execution has been successful or not

}

