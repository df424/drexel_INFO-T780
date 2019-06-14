
import tensorflow as tf
import numpy as np

def createModel(x_tensor, n_actions):
    input_layer = tf.reshape(x_tensor, (-1, 88, 88, 4))

    conv1 = tf.layers.conv2d(inputs=input_layer,
                             filters=32,
                             kernel_size=8,
                             strides=4,
                             activation=tf.nn.relu)

    conv2 = tf.layers.conv2d(inputs=conv1,
                             filters=64,
                             kernel_size=4,
                             strides=2,
                             activation=tf.nn.relu)

    conv3 = tf.layers.conv2d(inputs=conv2,
                             filters=64,
                             kernel_size=3,
                             strides=1,
                             activation=tf.nn.relu)
    
    dense1 = tf.layers.dense(inputs=conv3, units=512, activation=tf.nn.relu)
    outputs = tf.layers.dense(inputs=dense1, units=n, activation=None)
    return outputs