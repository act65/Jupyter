import numpy as np
def gen(shape):
    result = []
    for i in range(len(shape)-1):
        #initialise with values with random numbers between 0-1
        result.append(np.random.random((shape[i],shape[i+1])))
    return result   
    
def layer_index(ind,layers):
    """
    Map the layer index to a one hot list    
    
    >>> layer_index(2,4)
    >>> [0, 1, 0, 0]
    """
    result = [0] * (layers+1)
    result[ind-1] = 1
    return result

def logistic(z): #the logistic/sigmoid activation function
    return 1/(1+np.exp(-z))
