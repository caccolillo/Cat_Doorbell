
# import the opencv library 
import cv2 
  


width = 1920
height = 1080

# define a video capture object and set the image size
vid = cv2.VideoCapture(0) 
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

      
# Capture the video frame 1
ret, frame = vid.read() 
  
#save as a file
cv2.imwrite("frame1.png" , frame)    
 
#Capture the video frame 2
ret, frame = vid.read() 
  
#Save as a file
cv2.imwrite("frame2.png" , frame)    

# Capture the video frame 3
ret, frame = vid.read() 
  
#Save as a file
cv2.imwrite("frame3.png" , frame)    

# Capture the video frame 4
ret, frame = vid.read() 
  
#Save as a file
cv2.imwrite("frame4.png" , frame)    
      
  
#Release the cap object 
vid.release() 


