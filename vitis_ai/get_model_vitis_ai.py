
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#!wget https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
#!unzip -q kagglecatsanddogs_5340.zip
#!ls!ls PetImages

import os
from PIL import Image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import add
from tensorflow.keras.regularizers import l2
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import ZeroPadding2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import concatenate
from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.optimizers            import SGD
from tensorflow.keras.callbacks             import ModelCheckpoint, TensorBoard, LearningRateScheduler
import numpy as np
from sklearn.model_selection import train_test_split
import glob
import os
import tensorflow as tf
from tensorflow.io import read_file, write_file
from tensorflow.image import decode_image

def test_img(img_name,image_size):
    img = keras.utils.load_img(img_name, target_size=image_size)
    img_array = keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    predictions = model.predict(img_array)
    isacat = predictions[0, 0]
    isacat_flag = 0
    #print(predictions)
    if(isacat>0.7): 
        #print("++++++++++++++++++++++++++++++++++++")
        #print(predictions)
        #print("Image ",img_name," Is a cat at : ", isacat*100," % ") 
        #print("++++++++++++++++++++++++++++++++++++/n")
        isacat_flag = 1
        #isacat = predictions[0, 0]
        #isadog = predictions[0, 1]
        #print("Is a cat at :", isacat*100," % ") 
        #print("Is a dog at :", isadog*100," % ") 
    return isacat_flag    



# load our network weights from disk
print("[INFO] loading network...")

# load the trained model
model = tf.keras.models.load_model('./model_final.h5')
image_size = (180, 180)

print("[INFO] network...")

# Check the input and output name
print ("\n TF input node name:")
print(model.inputs)
print ("\n TF output node name:")
print(model.outputs)

input("*********")

isacat_flag = 0
numimages = 0
numcats = 0

directory = './PetImages/Cat/'
for filename in os.listdir(directory):
    filename = r"{}{}".format(directory,filename)
    isacat_flag = test_img(filename,image_size)
    numimages = numimages + 1
    if(isacat_flag==1): 
      numcats = numcats + 1
print("On ",numimages," ",numcats," were cats ")

input("Testing on cat folder completed. Press Enter to continue...")

isacat_flag = 0
numimages = 0
numcats = 0

directory = './PetImages/Dog/'
for filename in os.listdir(directory):
    filename = r"{}{}".format(directory,filename)
    isacat_flag = test_img(filename,image_size)
    numimages = numimages + 1
    if(isacat_flag==1): 
      numcats = numcats + 1
print("On ",numimages," ",numcats," were cats ")





