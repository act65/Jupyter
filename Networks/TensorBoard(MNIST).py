
# coding: utf-8

# In[ ]:

https://www.tensorflow.org/versions/r0.7/how_tos/graph_viz/index.html
https://www.tensorflow.org/versions/master/how_tos/summaries_and_tensorboard/index.html


# In[ ]:

import tensorflow as tf
import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

sess = tf.Session()

x = tf.placeholder("float", [None, 784])
y_ = tf.placeholder("float", [None, 10])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) + b)

cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

tf.scalar_summary('crossentropy', cross_entropy)
tf.histogram_summary('outputs', y_)
merged = tf.merge_all_summaries()
writer = tf.train.SummaryWriter("/tmp/mnist_logs",sess.graph.as_graph_def(add_shapes=True))

init = tf.initialize_all_variables()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    feed = {x: batch_xs, y_: batch_ys}
    if i%20 == 0:
        summary_str = sess.run(merged, feed_dict=feed)
        writer.add_summary(summary_str, i)
    else:
        sess.run(train_step, feed_dict=feed)
  
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
acc_val, b_val, W_val, Y = sess.run([accuracy, b ,W, y], feed_dict={x: mnist.test.images, y_: mnist.test.labels})
print('Accuracy = '+str(acc_val) + '%')


# In[ ]:

get_ipython().system('tensorboard --logdir=/tmp/mnist_logs')

