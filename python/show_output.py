# import the opencv library 
import cv2 
import numpy as np  

#read output image from txt file
def img_load_from_txt(name,frame,rows,columns,channels):
  pixel = 0
  file = open(name,'r')
  for i in range(channels):
    for j in range(rows):
      for k in range(columns):
        pixel = file.readline()
        #print(pixel)
        temp = int(pixel.strip()) 
        #print(temp)        
        frame[j,k,i] = temp
        #print(j,k,i) 
  file.close()



#set the image dimensions
rows = 960
columns = 1280
channels = 3       

#rows = 480
#columns = 640
#channels = 3   




#create a zeroed image array
frame = np.zeros([rows, columns, channels],dtype=np.uint8)
print(frame)

#read output image in txt format
img_load_from_txt("outputframe.txt" , frame, rows, columns, channels)    
  
#save as a png file
cv2.imwrite("output.png" , frame)    
       

