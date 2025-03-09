#quantize th h5 model for Vitis AI

import tensorflow as tf

from tensorflow_model_optimization.quantization.keras import vitis_quantize

float_model = tf.keras.models.load_model('./model_final.h5') #load the model

tf.saved_model.save(float_model, "models") #save as pb

print("**** successfully saved keras model file to tensorflow model file ****")

image_size = (180, 180)

batch_size = 128

train_ds, val_ds = tf.keras.utils.image_dataset_from_directory(
    "./kagglecatsanddogs_5340/PetImages",
    validation_split=0.2,
    subset="both",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

print("**** created dataset **** ")

quantizer = vitis_quantize.VitisQuantizer(float_model)

print("**** started quantizer **** ")

quantized_model = quantizer.quantize_model(calib_dataset=train_ds,add_shape_info=True)

print("**** quantized **** ")

quantized_model.save('quantized_model.h5')

print("**** saved quantized model **** ")
