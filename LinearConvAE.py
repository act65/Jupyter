import tensorflow as tf

w = 3
n = 28
s = 1

def steps(w,s,n):
    return (n-w+1)/s

x = tf.placeholder(tf.float32,shape=[None,28,28,1])
A = tf.Variable(tf.truncated_normal([w,w,1,1]))
B = tf.Variable(tf.truncated_normal([w,w,1,1]))
y = tf.conv2d_transpose(A,tf.conv2d(B,x))

m = steps(w,s,n)
#alternatively
v_x = tf.reshape(x,[None,784])

M_A = tf.zeros([784,m]) 
M_B = tf.zeros([m,784])

for i in range(m):
    for j in range(m):
        M_A[i+j*i:i+w+j*i] = A

y = tf.matmul(M_A,tf.matmul(M_B,v_x))
#how do we constrain this matrix?
