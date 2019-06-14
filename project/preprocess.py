
import numpy as np
from skimage.transform import resize
from skimage import color

def scaleImg(img):
    return resize(img, (88, 88), anti_aliasing=True)

def toGrayScale(img):
    return color.rgb2gray(img)


if __name__=='__main__':
    image = np.random.randint(0, 255, (160, 160, 3))
    print(image.shape)
    print(scaleImg(image).shape)