
import cv2 as cv
import numpy as np

def scaleImg(img):
    return cv.resize(img, dsize=(88,88), interpolation=cv.INTER_CUBIC)


if __name__=='__main__':
    image = np.random.randint(0, 255, (160, 160, 3))
    print(image.shape)
    print(scaleImg(image).shape)