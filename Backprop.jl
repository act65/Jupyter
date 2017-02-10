##

type Sigmoid{}
    function call{T}(z::??)

    end

    function grad{T}(z::??)

    end
end

##

type Relu{}
    function call{T}(z::??)
        (z>0).astype(float32())
    end

    function grad{T}(z::??)

    end
end

##

type Layer{shape, act_fn = Sigmoid,learning_rate::Float}
    act_fn = act_fn
    learning_rate = 0.0001
    weights = np.random.standard_normal(shape)#/np.sqrt(shape[0])
    biases = np.zeros((1,shape[-1]))

    function calc{T}(self,x)
        inputs = x
        activations = np.dot(x,weights)+biases
        outputs = act_fn.calc(activations)
    end

    function grad{T}(self,x,delta=None,train=False::Bool)
        calc(x) #this is the recompute tactic.
        # saves on memory, but requires more time.
        delta = np.ones((50,10)) #d_dY or should be identity?
        dYdZ = act_fn.grad(activations) #nxn
        d_dZ = np.dot(delta,dYdZ) if type(delta) == 'numpy.ndarray' else dYdZ #txn = txn x nxn
        d_dX = np.dot(d_dZ,weights.T) #
        if train: update(d_dZ) #update after calculating the delta for previous layer
        return d_dX
    end

    def update(self,d_dZ):
        weights -= learning_rate * np.dot(inputs.T,d_dZ) #dxn = dxN x Nxn
        biases = biases - learning_rate * d_dZ
