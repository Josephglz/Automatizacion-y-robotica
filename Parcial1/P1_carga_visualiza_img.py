import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from keras.api.utils import load_img, img_to_array

largo, alto = 100, 100
file = './woody.jpeg'

img = load_img(file, target_size = (largo, alto), color_mode = "grayscale")
print(img.size)
print(img.mode)

img.show()