import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from keras.api.utils import load_img, img_to_array

largo, alto = 180,180
file = './woody.jpeg'

img = load_img(file, target_size = (largo, alto), color_mode = "grayscale")
print(img.size)
print(img.mode)

import matplotlib.pyplot as plt
plt.imshow(img, cmap="gray")
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()