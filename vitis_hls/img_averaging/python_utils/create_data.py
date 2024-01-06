# import the libraries
import numpy as np
import argparse
import time
import cv2
import csv
import subprocess

#main function
# define a video capture object
vid = cv2.VideoCapture(0)
      
# Capture the video frame
# by frame
ret, frame = vid.read()
  
# Display the acquired frame
cv2.imshow(' frame ' , np.array(frame, dtype = np.uint8 ) )
cv2.waitKey(1)
time.sleep(12)

#save frame 1
ret, frame1 = vid.read()
np_frame1 = np.array(frame1).astype(np.uint8)
np_frame1_1d = np_frame1.reshape(-1)
# Save NumPy array to CSV file
np.savetxt('frame1.txt', np_frame1_1d, delimiter=',', fmt='%d')


#save frame 2
ret, frame2 = vid.read()
np_frame2 = np.array(frame2).astype(np.uint8)
np_frame2_1d = np_frame2.reshape(-1)
# Save NumPy array to CSV file
np.savetxt('frame2.txt', np_frame2_1d, delimiter=',', fmt='%d')


#save frame 3
ret, frame3 = vid.read()
np_frame3 = np.array(frame3).astype(np.uint8)
np_frame3_1d = np_frame3.reshape(-1)
# Save NumPy array to CSV file
np.savetxt('frame3.txt', np_frame3_1d, delimiter=',', fmt='%d')

#save frame 4
ret, frame4 = vid.read()
np_frame4 = np.array(frame4).astype(np.uint8)
np_frame4_1d = np_frame4.reshape(-1)
# Save NumPy array to CSV file
np.savetxt('frame4.txt', np_frame4_1d, delimiter=',', fmt='%d')


#get the averaged frame
frame1 =  np.array(frame1).astype(np.float32)
frame2 =  np.array(frame2).astype(np.float32)
frame3 =  np.array(frame3).astype(np.float32)
frame4 =  np.array(frame4).astype(np.float32)
average_frame = (frame1+frame2+frame3+frame4)/4

# Display the averaged frame
cv2.imshow(' averaged frame ' , np.array(average_frame, dtype = np.uint8 ) )
cv2.waitKey(1)
time.sleep(12)

np_average_frame = np.array(average_frame).astype(np.uint8)
np_average_frame_1d = np_average_frame.reshape(-1)
# Save NumPy array to CSV file
np.savetxt('average_frame.txt', np_average_frame_1d, delimiter=',', fmt='%d')


subprocess.call(["mv *.txt ./python_utils"], shell=True)

# closing all open windows
cv2.destroyAllWindows()
 
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
