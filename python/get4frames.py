
# # import the opencv library 
# import cv2 
  


# width = 1920
# height = 1080

# # define a video capture object and set the image size
# vid = cv2.VideoCapture(0) 
# vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

      
# # Capture the video frame 1
# ret, frame = vid.read() 
  
# #save as a file
# cv2.imwrite("frame1.png" , frame)    
 
# #Capture the video frame 2
# ret, frame = vid.read() 
  
# #Save as a file
# cv2.imwrite("frame2.png" , frame)    

# # Capture the video frame 3
# ret, frame = vid.read() 
  
# #Save as a file
# cv2.imwrite("frame3.png" , frame)    

# # Capture the video frame 4
# ret, frame = vid.read() 
  
# #Save as a file
# cv2.imwrite("frame4.png" , frame)    
      
  
# #Release the cap object 
# vid.release() 


# import the opencv library 
import cv2 
  

#save as a txt file
def img_save_as_txt(name,frame):

  #get the image dimensions
  image_dimensions = frame.shape
  print(image_dimensions)
  rows = image_dimensions[0]
  columns = image_dimensions[1]
  channel = image_dimensions[2] 
    
  file = open(name,'w')
  for i in range(channel):
    for j in range(rows):
      for k in range(columns):
        pixel = frame[j,k,i] 
        file.write('%d \n' % pixel)
  file.close()

width = 1920
height = 1080

# define a video capture object and set the image size
vid = cv2.VideoCapture(0) 
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
      
# Capture the video frame 1, 2, 3, 4
ret, frame1 = vid.read() 
ret, frame2 = vid.read() 
ret, frame3 = vid.read() 
ret, frame4 = vid.read() 
  
#save as a png file
cv2.imwrite("frame1.png" , frame1)    
cv2.imwrite("frame2.png" , frame2)    
cv2.imwrite("frame3.png" , frame3)    
cv2.imwrite("frame4.png" , frame4)        

#save as a txt file
img_save_as_txt("frame1.txt" , frame1)
img_save_as_txt("frame2.txt" , frame2)
img_save_as_txt("frame3.txt" , frame3)
img_save_as_txt("frame4.txt" , frame4)

#Release the cap object 
vid.release() 