# https://keras.io/examples/vision/image_classification_from_scratch/

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#!wget https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
#!unzip -q kagglecatsanddogs_5340.zip
#!ls!ls PetImages

import os
from PIL import Image



# import the necessary packages
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



#detect invalid images in the dataset and delete them
should_rewrite_image = True # set to true if you are getting Corrupt Data error
num_skipped = 0
for folder_name in ("Cat", "Dog"):
    folder_path = os.path.join('./PetImages', folder_name)
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        is_jfif = True
        should_remove = False
        
        with open(fpath, "rb") as fobj:
            is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
            
        try:
            img = read_file(fpath)
            if not tf.io.is_jpeg(img):
                should_remove = True
                
            img = decode_image(img)

            if img.ndim != 3:
                should_remove = True

        except Exception as e:
            should_remove = True
        
        if (not is_jfif) or should_remove:
            num_skipped += 1
            # Delete corrupted image
            os.remove(fpath)
        elif should_rewrite_image:
            tmp = tf.io.encode_jpeg(img)
            write_file(fpath, tmp)

print("Deleted %d images" % num_skipped)






NUM_EPOCHS = 5
INIT_LR = 0.05
image_size = (180, 180)
BATCH_SIZE = 32

weights = "./"
fname = os.path.sep.join([weights, "best_chkpt.hdf5"])
checkpoint = ModelCheckpoint(fname,
		monitor="val_loss", mode="min",
		#monitor="val_acc", mode="max",
		save_best_only=True, verbose=1)

callbacks_list = [checkpoint]

train_ds, val_ds = tf.keras.utils.image_dataset_from_directory(
    "./PetImages",
    validation_split=0.2,
    subset="both",
    seed=1337,
    image_size=image_size,
    batch_size=BATCH_SIZE,
)

for image_batch, labels_batch in val_ds:
  x_valid = image_batch.numpy()
  y_valid = labels_batch.numpy()
  break

for image_batch, labels_batch in train_ds:
  x_train = image_batch.numpy()
  y_train = labels_batch.numpy()
  break

import matplotlib.pyplot as plt


x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, random_state=0, train_size = .75)




data_augmentation = keras.Sequential(
    [
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
    ]
)

# data genarators
test_datagen =ImageDataGenerator()
train_datagen =ImageDataGenerator()
valid_datagen=ImageDataGenerator()
aug_datagen = ImageDataGenerator(
        #rescale=1/255,
        rotation_range=5,
        horizontal_flip=True,
        height_shift_range=0.1,
        width_shift_range=0.1,
        shear_range=0.2,
        zoom_range=0.2)

aug_generator = aug_datagen.flow(
        x_train, y_train,
        batch_size=BATCH_SIZE)

train_generator = train_datagen.flow(
        x_train, y_train,
        batch_size=BATCH_SIZE)

validation_generator = valid_datagen.flow(
        x_valid, y_valid,
        batch_size=BATCH_SIZE)

pred_generator = test_datagen.flow(
        x_test, y_test,
        batch_size=1)



def make_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)

    # Entry block
    x = layers.Rescaling(1.0 / 255)(inputs)
    x = layers.Conv2D(128, 3, strides=2, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    for size in [256, 512, 728]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = layers.Conv2D(size, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    x = layers.SeparableConv2D(1024, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.GlobalAveragePooling2D()(x)
    if num_classes == 2:
        activation = "sigmoid"
        units = 1
    else:
        activation = "softmax"
        units = num_classes

    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(units, activation=activation)(x)
    return keras.Model(inputs, outputs)

# model taken from:
# https://github.com/Xilinx/Vitis-AI-Tutorials/blob/3.0/Tutorials/Keras_GoogleNet_ResNet/files/code/custom_cnn.py

def residual_module(data, K, stride, chanDim, red=False, reg=0.0001, bnEps=2e-5, bnMom=0.9):
    # the shortcut branch of the ResNet module should be initialized as the input (identity) data
    shortcut = data
    # the first block of the ResNet module are the 1x1 CONVs
    bn1 = BatchNormalization(axis=chanDim, epsilon=bnEps,momentum=bnMom)(data)
    act1 = Activation("relu")(bn1)
    conv1 = Conv2D(int(K * 0.25), (1, 1), use_bias=False, kernel_regularizer=l2(reg))(act1)
    # the second block of the ResNet module are the 3x3 CONVs
    bn2 = BatchNormalization(axis=chanDim, epsilon=bnEps,momentum=bnMom)(conv1)
    act2 = Activation("relu")(bn2)
    conv2 = Conv2D(int(K * 0.25), (3, 3), strides=stride, padding="same", use_bias=False, kernel_regularizer=l2(reg))(act2)
    # the third block of the ResNet module is another set of 1x1 CONVs
    bn3 = BatchNormalization(axis=chanDim, epsilon=bnEps, momentum=bnMom)(conv2)
    act3 = Activation("relu")(bn3)
    conv3 = Conv2D(K, (1, 1), use_bias=False, kernel_regularizer=l2(reg))(act3)
    # if we are to reduce the spatial size, apply a CONV layer to the shortcut
    if red:
        shortcut = Conv2D(K, (1, 1), strides=stride, use_bias=False, kernel_regularizer=l2(reg))(act1)
    # add together the shortcut and the final CONV
    x = add([conv3, shortcut])
    # return the addition as the output of the ResNet module
    return x




def miniResNet(width, height, depth, classes, stages, filters, reg=0.0001, bnEps=2e-5, bnMom=0.9):
                # initialize the input shape to be "channels last" and the channels dimension itself
                inputShape = (height, width, depth)
                chanDim = -1
                # if we are using "channels first", update the input shape and channels dimension
                if K.image_data_format() == "channels_first":
                        inputShape = (depth, height, width)
                        chanDim = 1
                # set the input and apply BN
                inputs = Input(shape=inputShape, name="conv2d_1_input")
                x = BatchNormalization(axis=chanDim, epsilon=bnEps, momentum=bnMom)(inputs)
                             
                #we are using the Tiny ImageNet dataset
                # apply CONV => BN => ACT => POOL to reduce spatial size
                x = Conv2D(filters[0], (5, 5), use_bias=False, padding="same", kernel_regularizer=l2(reg))(x)
                x = BatchNormalization(axis=chanDim, epsilon=bnEps, momentum=bnMom)(x)
                x = Activation("relu")(x)
                x = ZeroPadding2D((1, 1))(x)
                x = MaxPooling2D((3, 3), strides=(2, 2))(x)
                # loop over the number of stages
                for i in range(0, len(stages)):
                        # initialize the stride, then apply a residual module used to reduce the spatial size of the input volume
                        stride = (1, 1) if i == 0 else (2, 2)
                        x = residual_module(x, filters[i + 1], stride, chanDim, red=True, bnEps=bnEps, bnMom=bnMom)
                        # loop over the number of layers in the stage
                        for j in range(0, stages[i] - 1):
                                # apply a ResNet module
                                x = residual_module(x, filters[i + 1],(1, 1), chanDim, bnEps=bnEps, bnMom=bnMom)
                # apply BN => ACT => POOL
                x = BatchNormalization(axis=chanDim, epsilon=bnEps, momentum=bnMom)(x)
                x = Activation("relu")(x)
                x = AveragePooling2D((8, 8))(x)
                # softmax classifier
                x = Flatten()(x)
                x = Dense(classes, kernel_regularizer=l2(reg))(x)
                x = Activation("softmax")(x)
                # create the model
                model = Model(inputs, x, name="resnet")
                # return the constructed network architecture
                return model


def test_img(img_name,image_size):
    img = keras.utils.load_img(img_name, target_size=image_size)
    img_array = keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    predictions = model.predict(img_array)
    isacat = predictions[0, 1]
    isacat_flag = 0
    if(isacat>0.7): 
        print("++++++++++++++++++++++++++++++++++++")
        #print(predictions)
        print("Image ",img_name," Is a cat at : ", isacat*100," % ") 
        print("++++++++++++++++++++++++++++++++++++/n")
        isacat_flag = 1
        #isacat = predictions[0, 0]
        #isadog = predictions[0, 1]
        #print("Is a cat at :", isacat*100," % ") 
        #print("Is a dog at :", isadog*100," % ") 
    return isacat_flag    


model = miniResNet(width=image_size[0],height=image_size[1],depth=3,classes=2,stages=(9, 9, 9),filters=(64, 64, 128, 256),reg=0.0005)
keras.utils.plot_model(model, show_shapes=True)
model.summary()

#epochs = 10
epochs = 1
callbacks = [
    keras.callbacks.ModelCheckpoint("save_at_{epoch}.keras"),
]

opt = SGD(lr=INIT_LR, momentum=0.9)
model.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

model.fit(
   train_ds,
   epochs=epochs,
   callbacks=callbacks,
   validation_data=val_ds,
)

input("Training completed. Press Enter to continue...")

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

input("Testing completed. Press Enter to continue...")

# save trained weights
WEIGHTS_FINAL = 'model_final.h5'
model.save(WEIGHTS_FINAL)

from tensorflow_model_optimization.quantization.keras import vitis_quantize
# do quantization
calib_dataset = val_ds
quant_model = vitis_quantize.VitisQuantizer(model).quantize_model(
      calib_dataset=calib_dataset,
      add_shape_info=True)
# quant_model.summary()
q_save_path = os.path.join('./quantized', 'quantized.h5')
quant_model.save(q_save_path)
print("\n***************** Summary *****************")
print("Quantized model is saved in ", q_save_path)
