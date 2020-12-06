import numpy as np
### methods to use  np.zeros,np.ones,np.random.rand

## returns bias vector for specific number of neurons
## T_Layer : The number of neurons in this layer
def get_bias(T_Layer):
    return np.zeros(T_Layer)

## returns weights matrix for specific number of neurons in this layer and the layer before
## T_Layer : The number of neurons in this layer
## L_Layer : The number of neurons in the last layer
def get_weights(L_Layer,T_Layer):
    return np.random.rand(T_Layer,L_Layer)





