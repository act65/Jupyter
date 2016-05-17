#https://github.com/tensorflow/tensorflow/blob/r0.8/tensorflow/examples/tutorials/mnist/mnist_with_summaries.py

import tensorflow as tf

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_integer('batch_size', 10, 'Number of samples to train on for SGD')

