
# import the libraries
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from keras.applications import imagenet_utils
from imutils.object_detection import non_max_suppression
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

#image pre-processing function  
def preprocessing(frame):
   # convert the image to grayscale format
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('grayscale', img_gray)

    #histogram equalization
    gray_img_eqhist=cv2.equalizeHist(img_gray)
    #cv2.imshow('grayscale histogram equalized', gray_img_eqhist)

    #denoise grayscale
    ddenoised = cv2.fastNlMeansDenoising(gray_img_eqhist,  None, 3, 4, 2)
    #cv2.imshow('grayscale denoised', ddenoised)

    #gaussian blurring
    blur = cv2.GaussianBlur(ddenoised,(5,5),0)
    #cv2.imshow('grayscale blurred', blur)

    #Otsu thresholding
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #cv2.imshow('thresholded', th3)
    
    #edge detection
    edgedet = cv2.Canny(image=blur, threshold1=120, threshold2=200) # Combined X and Y Sobel Edge Detection
    #cv2.imshow('edge detected', edgedet)

    #find the intersection of edge detected and binarized
    img_bwa = cv2.bitwise_and(th3,edgedet)
    #cv2.imshow('intersection ', img_bwa)

    #erosion
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.dilate(img_bwa,kernel,iterations = 1)   
    #cv2.imshow('eroded intersection ', erosion)

    #returns 
    return erosion, blur

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


def image_detection(image,min_conf):
  stepSize = 100 #stride (10)
  (w_width, w_height) = (150, 200) # search window size
  for x in range(0, image.shape[1] - w_width , stepSize):
     for y in range(0, image.shape[0] - w_height, stepSize):
        window = image[x:x + w_width, y:y + w_height, :]
        cv2.imshow('roi' , np.array(window, dtype = np.uint8 ) )
        cv2.waitKey(1)
        time.sleep(0.12)
        tmp = image.copy()
        cv2.rectangle(tmp, (x, y), (x + w_width, y + w_height), (255, 0, 0), 2) # draw rectangle on image
        cv2.imshow('scan window' , np.array(tmp, dtype = np.uint8 ) )
        cv2.waitKey(1) 
        time.sleep(0.12)
        #classify with resnet50
        image_resnet50 = cv2.resize(window, (224, 224)) #resize in the format expected by resnet50

        image_resnet50 = img_to_array(image_resnet50) #convert to numpy array
        #image_resnet50 = cv2.cvtColor(image_resnet50, cv2.COLOR_RGB2BGR)
        #image_resnet50 = imagenet_utils.preprocess_input(image_resnet50) #puts data in a range of values expected by resnet50
        #image_resnet50 = tf.keras.applications.mobilenet.preprocess_input(image_resnet50)
        cv2.imshow('scan window resnet' , np.array(image_resnet50, dtype = np.uint8 ) )
        cv2.waitKey(1) 
        time.sleep(0.12) 
 
        image_resnet50 = np.expand_dims(image_resnet50, axis=0) #adds a dimension to the image
        preds = model.predict(image_resnet50) #predicts the ROI by using resnet50

        preds = imagenet_utils.decode_predictions(preds, top=1)
        labels = {}
        locs = []
        # loop over the predictions
        for (i, p) in enumerate(preds):
            # grab the prediction information for the current ROI
            (imagenetID, label, prob) = p[0]
            # filter out weak detections by ensuring the predicted probability
            # is greater than the minimum probability
            if prob >= min_conf:
                # grab the bounding box associated with the prediction and
                # convert the coordinates
                locs.append((x, y, x + w_width, y + w_height))
                box = locs[i]
                # grab the list of predictions for the label and add the
                # bounding box and probability to the list
                L = labels.get(label, [])
                L.append((box, prob))
                labels[label] = L
  return labels
  


# def image_detection(orig,min_conf):

#   # resize the image such that it has the
#   # has the supplied width, and then grab its dimensions
#   orig = imutils.resize(orig, width=WIDTH)
#   (H, W) = orig.shape[:2]

#   # initialize the image pyramid
#   pyramid = image_pyramid(orig, scale=PYR_SCALE, minSize=ROI_SIZE)

#   # initialize two lists, one to hold the ROIs generated from the image
#   # pyramid and sliding window, and another list used to store the
#   # (x, y)-coordinates of where the ROI was in the original image
#   rois = []
#   locs = []
#   # time how long it takes to loop over the image pyramid layers and
#   # sliding window locations
#   start = time.time()

#   # loop over the image pyramid
#   for image in pyramid:
#       # determine the scale factor between the *original* image
#       # dimensions and the *current* layer of the pyramid
#       scale = W / float(image.shape[1])
#       # for each layer of the image pyramid, loop over the sliding
#       # window locations
#       for (x, y, roiOrig) in sliding_window(image, WIN_STEP, ROI_SIZE):
#           # scale the (x, y)-coordinates of the ROI with respect to the
#           # *original* image dimensions
#           x = int(x * scale)
#           y = int(y * scale)
#           w = int(ROI_SIZE[0] * scale)
#           h = int(ROI_SIZE[1] * scale)
#           # take the ROI and preprocess it so we can later classify
#           # the region using Keras/TensorFlow
#           roi = cv2.resize(roiOrig, INPUT_SIZE)
#           # Display the resulting frame
#           cv2.imshow(' roi orig', roiOrig)

#           cv2.imshow(' roi ', roi)
#           time.sleep(0.5)
#           roi = img_to_array(roi)
#           roi = preprocess_input(roi)
#           # update our list of ROIs and associated coordinates
#           rois.append(roi)
#           locs.append((x, y, x + w, y + h))
#           # check to see if we are visualizing each of the sliding
#           # windows in the image pyramid
#           # clone the original image and then draw a bounding box
#           # surrounding the current region
#           clone = orig.copy()
#           cv2.rectangle(clone, (x, y), (x + w, y + h),(0, 255, 0), 2)
	
#   # show how long it took to loop over the image pyramid layers and
#   # sliding window locations
#   end = time.time()
#   print("[INFO] looping over pyramid/windows took {:.5f} seconds".format(end - start))
#   # convert the ROIs to a NumPy array
#   rois = np.array(rois, dtype="float32")
#   # classify each of the proposal ROIs using ResNet and then show how
#   # long the classifications took
#   print("[INFO] classifying ROIs...")
#   start = time.time()
#   preds = model.predict(rois)
#   end = time.time()
#   print("[INFO] classifying ROIs took {:.5f} seconds".format(end - start))
#   # decode the predictions and initialize a dictionary which maps class
#   # labels (keys) to any ROIs associated with that label (values)
#   preds = imagenet_utils.decode_predictions(preds, top=1)
#   labels = {}
#   # loop over the predictions
#   for (i, p) in enumerate(preds):
#       # grab the prediction information for the current ROI
#       (imagenetID, label, prob) = p[0]
#       # filter out weak detections by ensuring the predicted probability
#       # is greater than the minimum probability
#       if prob >= min_conf:
#           # grab the bounding box associated with the prediction and
#           # convert the coordinates
#           box = locs[i]
#           # grab the list of predictions for the label and add the
#           # bounding box and probability to the list
#           L = labels.get(label, [])
#           L.append((box, prob))
#           labels[label] = L
#       # loop over the labels for each of detected objects in the image
#   for label in labels.keys():
#       # clone the original image so that we can draw on it
#       print("[INFO] showing results for '{}'".format(label))
#       clone = orig.copy()
#       # loop over all bounding boxes for the current label
#       for (box, prob) in labels[label]:
#           # draw the bounding box on the image
#           (startX, startY, endX, endY) = box
#           cv2.rectangle(clone, (startX, startY), (endX, endY),(0, 255, 0), 2)
#       # show the results *before* applying non-maxima suppression, then
#       # clone the image again so we can display the results *after*
#       # applying non-maxima suppression
#       clone = orig.copy()
#       # extract the bounding boxes and associated prediction
#       # probabilities, then apply non-maxima suppression
#       boxes = np.array([p[0] for p in labels[label]])
#       proba = np.array([p[1] for p in labels[label]])
#       boxes = non_max_suppression(boxes, proba)
#       # loop over all bounding boxes that were kept after applying
#       # non-maxima suppression
#       for (startX, startY, endX, endY) in boxes:
#           # draw the bounding box and label on the image
#           cv2.rectangle(clone, (startX, startY), (endX, endY),(0, 255, 0), 2)
#           y = startY - 10 if startY - 10 > 10 else startY + 10
#           cv2.putText(clone, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
#   return clone











#main function
# define a video capture object
vid = cv2.VideoCapture(0)


# initialize variables used for the object detection procedure
WIDTH = 800
PYR_SCALE = 1.5
WIN_STEP = 50
ROI_SIZE = (200,200)
INPUT_SIZE = (224, 224)
min_conf = 0.15 #minimum confidence level
# load our network weights from disk
print("[INFO] loading network...")
model = ResNet50(weights="imagenet", include_top=True)




while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  


    # Display the resulting frame
    cv2.imshow(' frame ', frame)
      
    avg = img_averaging(vid)
    cv2.imshow(' averaged ', avg)


    erosion, blur = preprocessing(avg)
    #cv2.imshow(' eroded intersection ', erosion)
    #cv2.imshow(' blurred  ', blur)
    # image detection with CNN tutorial
    # https://pyimagesearch.com/2020/06/22/turning-any-cnn-image-classifier-into-an-object-detector-with-keras-tensorflow-and-opencv/
    detected = image_detection(avg,min_conf)
    print(detected)
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
