import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from keras.api.utils import load_img, img_to_array

largo, alto = 180,180
file = './woody.jpeg'

img = load_img(file, target_size = (largo, alto), color_mode = "grayscale")
print(img.size)
print(img.mode)

img_en_array = img_to_array(img)
print(img_en_array.shape)

# print(img_en_array)

archivo = open("woody_data.csv", "w")
for i in img_en_array:
    for j in i:
        archivo.write(str(j[0]) + ",")
    archivo.write("\n")
archivo.flush()
archivo.close()