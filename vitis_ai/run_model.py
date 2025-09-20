import numpy as np
import cv2
import vitis_ai_library
import xir
from IPython.display import Image

print('*')
# file path
MODEL_PATH = "customcnn.xmodel"
IMG_PATH = "cat.jpg"
# Load model and Create Instance
g = xir.Graph.deserialize(MODEL_PATH)
print('** graph deserialize')
runner = vitis_ai_library.GraphRunner.create_graph_runner(g)
print('*** graph runner')
## Prepare input/output buffers 
# input buffer
inputDim = tuple(runner.get_inputs()[0].get_tensor().dims)
print('**** input dim')
inputData = [np.empty(inputDim, dtype=np.int8)]
print('***** input data')
# input image
image = cv2.imread(IMG_PATH, cv2.IMREAD_COLOR)  
print('****** input image')
# normalization
image = image/255.0
print('******* normalization')
# quantization
fix_point = runner.get_input_tensors()[0].get_attr("fix_point")
print('******** quantization')
scale = 2 ** fix_point
image = (image * scale).round()
print('********* scale')
image = image.astype(np.int8)
print('**********')
# set input data
inputData[0][0] = cv2.resize(image,(180,180))
print('***********')
# output buffer
outputData = runner.get_outputs()
print('************')
# prediction
job_id = runner.execute_async(inputData, outputData)
print('************* execute runner')
runner.wait(job_id)
print('**************')
print(outputData)
#confirmation of prediction results
resultList = np.asarray(outputData[0])[0]
print('***************')
print(resultList)
resultIdx = resultList.argmax()
resultVal = resultList[resultIdx]
print("Predictions")
for i, x in enumerate(resultList):
    print("%d : %f"%(i, x))
#delete instance
del runner    
