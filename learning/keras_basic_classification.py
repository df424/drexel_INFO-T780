
import matplotlib.pyplot as plt

def plotHistory(history):
    f, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(history.history['acc'])
    ax1.plot(history.history['val_acc'])
    ax1.legend(['train', 'test'])
    ax1.set_title('Accuracy')
    ax2.plot(history.history['loss'])
    ax2.plot(history.history['val_loss'])
    ax2.legend(['train', 'test'])
    ax2.set_title('Loss')
    plt.show()