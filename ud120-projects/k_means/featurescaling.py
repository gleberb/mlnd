""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
from __future__ import division
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def featureScaling(arr):
    #minimum = min(arr)
    #maximum = max(arr)
    #result=[]
    #for d in arr:
    #    scaled = (d-minimum)/(maximum-minimum)
    #    result.append(scaled)
    scaler = MinMaxScaler()
    arr_reshape = np.reshape(arr, (-1, 1))
    result = scaler.fit_transform(arr_reshape)
    return result
# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
