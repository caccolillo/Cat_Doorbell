
# import the libraries
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from keras.applications import imagenet_utils
from imutils.object_detection import non_max_suppression
from tensorflow.python.keras.models import load_model
import numpy as np
import argparse
import imutils
import time
import cv2
import matplotlib.pyplot as plt
from keras.applications import ResNet50
from keras.applications import imagenet_utils

#sliding window function
def sliding_window(image, step, ws):
    # slide a window across the image
    for y in range(0, image.shape[0] - ws[1], step):
        for x in range(0, image.shape[1] - ws[0], step):
            # yield the current window
            yield (x, y, image[y:y + ws[1], x:x + ws[0]])

#create image pyramid
def image_pyramid(image, scale=1.5, minSize=(224, 224)):
    # yield the original image
    yield image
    # keep looping over the image pyramid
    while True:
        # compute the dimensions of the next image in the pyramid
        w = int(image.shape[1] / scale)
        image = imutils.resize(image, width=w)
        # if the resized image does not meet the supplied minimum
        # size, then stop constructing the pyramid
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
        # yield the next image in the pyramid
        yield image

# #image pre-processing function  
# def preprocessing(frame):
#    # convert the image to grayscale format
#     img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     #cv2.imshow('grayscale', img_gray)

#     #histogram equalization
#     gray_img_eqhist=cv2.equalizeHist(img_gray)
#     #cv2.imshow('grayscale histogram equalized', gray_img_eqhist)

#     #denoise grayscale
#     ddenoised = cv2.fastNlMeansDenoising(gray_img_eqhist,  None, 3, 4, 2)
#     #cv2.imshow('grayscale denoised', ddenoised)

#     #gaussian blurring
#     blur = cv2.GaussianBlur(ddenoised,(5,5),0)
#     #cv2.imshow('grayscale blurred', blur)

#     #Otsu thresholding
#     ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#     #cv2.imshow('thresholded', th3)
    
#     #edge detection
#     edgedet = cv2.Canny(image=blur, threshold1=120, threshold2=200) # Combined X and Y Sobel Edge Detection
#     #cv2.imshow('edge detected', edgedet)

#     #find the intersection of edge detected and binarized
#     img_bwa = cv2.bitwise_and(th3,edgedet)
#     #cv2.imshow('intersection ', img_bwa)

#     #erosion
#     kernel = np.ones((3,3),np.uint8)
#     erosion = cv2.dilate(img_bwa,kernel,iterations = 1)   
#     #cv2.imshow('eroded intersection ', erosion)

#     #returns 
#     return erosion, blur


#image pre-processing function  
def preprocessing(frame):
  tmp = frame.copy()
  #illumination correction using CLAHE
  img = cv2.cvtColor(tmp, cv2.COLOR_RGB2Lab)
  #configure CLAHE
  clahe = cv2.createCLAHE(clipLimit=10,tileGridSize=(8,8))
  #0 to 'L' channel, 1 to 'a' channel, and 2 to 'b' channel
  img[:,:,0] = clahe.apply(img[:,:,0])
  img = cv2.cvtColor(img, cv2.COLOR_Lab2RGB)
  cv2.imshow("CLAHE", img)
  #cv2.waitKey(0)
  #cv2.destroyAllWindows()
  #image denoising 
  tmp2 = frame.copy()
  noiseless_image_colored = cv2.fastNlMeansDenoisingColored(tmp2,None,20,20,7,21) 
  cv2.imshow("Denoised", img)
  #cv2.waitKey(0)
  #cv2.destroyAllWindows() 

  return noiseless_image_colored

#frame averaging
def img_averaging(vid):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    np_frame = np.array(frame).astype(np.float32)
    
    ret, frame1 = vid.read()
    np_frame1 = np.array(frame1).astype(np.float32)
    
    ret, frame2 = vid.read()
    np_frame2 = np.array(frame2).astype(np.float32)
    
    ret, frame3 = vid.read()
    np_frame3 = np.array(frame3).astype(np.float32)
    
    average_frame = (np_frame+np_frame1+np_frame2+np_frame3)/4
    average_frameint = average_frame .astype(np.uint8)
    return average_frameint


def image_detection(image,min_conf,stepSize):
  #stepSize = 100 #stride (10)
  locs = np.array([0,0,0,0,0])
  entry = np.array([0,0,0,0,0])
  first_det = True
  (w_width, w_height) = (150, 200) # search window size
  for x in range(0, image.shape[1] - w_width , stepSize):
     for y in range(0, image.shape[0] - w_height, stepSize):
        window = image[x:x + w_width, y:y + w_height, :]
        cv2.imshow('roi' , np.array(window, dtype = np.uint8 ) )
        cv2.waitKey(1)
        time.sleep(0.12)
        tmp = image.copy()
        #cv2.rectangle(tmp, (x, y), (x + w_width, y + w_height), (255, 0, 0), 2) # draw rectangle on image
        #cv2.imshow('scan window' , np.array(tmp, dtype = np.uint8 ) )
        #cv2.waitKey(1) 
        time.sleep(0.12)
        #classify with resnet50
        image_resnet50 = cv2.resize(window, (180, 180)) #resize in the format expected by resnet50
        image_resnet50 = img_to_array(image_resnet50) #convert to numpy array
        #cv2.imshow('scan window resnet' , np.array(image_resnet50, dtype = np.uint8 ) )
        #cv2.waitKey(1) 
        #time.sleep(0.12) 
 
        image_resnet50 = np.expand_dims(image_resnet50, axis=0) #adds a dimension to the image
        preds = model.predict(image_resnet50)[0] #predicts the ROI by using resnet50
        print(preds)
        score = float(preds[0])
        #print(f"This image is {100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog.")
        prob_cat = 1 - score
        prob_dog = score

        # filter out weak detections by ensuring the predicted probability
        # is greater than the minimum probability
        if prob_cat >= min_conf:
            entry = [x, y, x + w_width, y + w_height, prob_cat]
            locs = np.vstack((locs,entry))
  return locs
  
def draw_bounding_box(image,locs):
    entry = np.array([0,0,0,0,0])
    #print(len(locs.shape))
    #print(locs.ndim)
    if(sum(locs.shape)>5):
      clone = image.copy()
      # extract the bounding boxes and associated prediction
      # probabilities, then apply non-maxima suppression
      boxes = locs[:,[0,1,2,3]]
      boxes = boxes.astype(int)
      proba = locs[:,4]
      boxes = non_max_suppression(boxes, proba)
      print(boxes)
      # loop over all bounding boxes that were kept after applying
      # non-maxima suppression
      i=0
      for (startX, startY, endX, endY) in boxes:
        if(not(startX==0 and startY==0 and endX==0 and endY==0)):
          # draw the bounding box and label on the image
          cv2.rectangle(clone, (startX, startY), (endX, endY),(0, 255, 0), 2)
          y = startY - 10 if startY - 10 > 10 else startY + 10
          cv2.putText(clone, 'cat', (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
      return clone
    else:
      if(locs[4]>0.0):
        boxes = locs[0:3]
        boxes = boxes.astype(int)
        (startX, startY, endX, endY)=boxes
        cv2.rectangle(image, (startX, startY), (endX, endY),(0, 255, 0), 2)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.putText(image, 'cat', (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)        
      return image

#main function
# define a video capture object
vid = cv2.VideoCapture(0)


# initialize variables used for the object detection procedure
WIDTH = 800
PYR_SCALE = 1.5
stepSize = 50 #stride (10)
ROI_SIZE = (200,200)
INPUT_SIZE = (224, 224)
min_conf = 0.97 #minimum confidence level
# load our network weights from disk
print("[INFO] loading network...")

# load the trained model
model = tf.keras.models.load_model('./model_final.h5')


while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  


    # Display the resulting frame
    cv2.imshow(' frame ', frame)
      
    avg = img_averaging(vid)
    avg_clone = avg.copy()

    cv2.imshow(' averaged ', avg)


    prep = preprocessing(avg)
    #cv2.imshow(' eroded intersection ', erosion)
    #cv2.imshow(' blurred  ', blur)
    # image detection with CNN tutorial
    # https://pyimagesearch.com/2020/06/22/turning-any-cnn-image-classifier-into-an-object-detector-with-keras-tensorflow-and-opencv/
    detected = image_detection(prep,min_conf,stepSize)
    print(detected)

    detected_image=draw_bounding_box(avg,detected)
    cv2.imshow(' detected ', detected_image)
   
    #cv2.imshow(' detected  ', detected)
    #motion detection
    #https://www.life2coding.com/opencv-simple-motion-detection/

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # closing all open windows
        cv2.destroyAllWindows()
        #quit
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
