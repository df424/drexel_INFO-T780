
# This file follows the tutorial from https://www.tensorflow.org/tutorials/keras/basic_classification as per the instructions...

import tensorflow as tf
from tensorflow import keras
import numpy as np

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Load the data using keras' built in functions...
(train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()


def createBasicANN(input_shape, n_outputs, layers, activation):
    _layers = [keras.layers.Flatten(input_shape=input_shape)]

    for l in layers:
        _layers.append(l, activation = activation)

    _layers.append(n_outputs, activation=tf.nn.softmax)


[[1, 0, 0, 1, 0, 0, 1, 0],
[1, 0, 0, 1, 0, 0, 1, 1],
[0, 1, 0, 1, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 1],
[0, 1, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 1, 0],
[1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 0, 0, 0],
[1, 0, 0, 0, 1, 0, 0, 1],
[0, 1, 0, 0, 1, 0, 1, 1],
[0, 1, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 0, 1, 1]]