
[Neural Programmer-Interpreters](http://arxiv.org/abs/1511.06279)

Three parts;

* RNN
* Memory
* Domain-specific encoder


### RNN

A LSTM. Eww

##### Decoders
All from the same hidden layer.

* end-of-program probability, 
* program key embedding, 
* and output arguments.


##### Curriculum learning. 
Now we have input-output pairs to train on. Very similar to traditional feed forward? What is the difference between this and sequence-to-sequence learning?

How can we get this type of data for other domains? Possible because we know what the steps required are to get from A to B. 

### Memory

> a learnable key-value memory of program embeddings

> … program embeddings … are stored in a learnable persistent memory. The programs therefore have a more succinct representation than neural programs encoded as the full set of weights in a neural network


Does it learn the programs stored in memory???

Relation to functional programming? 

### Domain-specific encoder




# Questions

* Any relation to interpreter vs compiler?
* How does it learn the lower-level programs that are composed?
* Does this learn to generalise or to copy?
* So it is learning to be a controller? Not …?
* Relation to reinforcement learning - learning a series of actions in an environment??
* Could this sort of algrithm find faster approximations to well known algorithms? If we add regularisatin for how manu steps it takes??