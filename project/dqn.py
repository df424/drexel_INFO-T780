
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

def createModel(n_actions):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=8, strides=4, activation='relu', input_shape=(88,88,1)))
    model.add(Conv2D(64, kernel_size=4, strides=2, activation='relu'))
    model.add(Conv2D(64, kernel_size=3, strides=1, activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(n_actions, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model