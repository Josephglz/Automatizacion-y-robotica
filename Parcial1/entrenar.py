import os
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.api.models import Sequential
from keras.api.layers import Dropout, Flatten, Dense, Activation
from keras.api.layers import Convolution2D, MaxPooling2D
from keras import backend as K

K.clear_session()

data_entrenamiento = "./Parcial1/ConvolutionalNeuronal/F1-Entrenamiento"
data_validacion = "./Parcial1/ConvolutionalNeuronal/F2-Validacion"

# Parámetros
epocas = 30
alto, largo = 300, 300
batch_size = 10
pasos = 8
pasos_validacion = 3

kernel1 = (3, 3)
kernel2 = (2, 2)
kernel3 = (3, 3)

# Reducción de número de kernels
tot_kernels1 = 16  
tot_kernels2 = 32
tot_kernels3 = 64

stride = (2, 2)

clases = 4
lr = 0.001  # learning rate

# Aumento de datos con más variaciones
entrenamiento_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.4,  # Aumento de la inclinación
    zoom_range=0.4,   # Aumento del zoom
    vertical_flip=True,
    horizontal_flip=True,
    rotation_range=30,  # Rotaciones adicionales
    width_shift_range=0.2,  # Desplazamiento horizontal
    height_shift_range=0.2  # Desplazamiento vertical
)

prueba_datagen = ImageDataGenerator(rescale=1./255)

imagen_entrenamiento = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(alto, largo),
    batch_size=batch_size,
    class_mode='categorical',
    color_mode="grayscale"
)

imagen_prueba = prueba_datagen.flow_from_directory(
    data_validacion,
    target_size=(alto, largo),
    batch_size=batch_size,
    class_mode='categorical',
    color_mode="grayscale"
)

# Red convolucional
cnn = Sequential()

# Capa 1: Reducción de número de kernels
cnn.add(Convolution2D(tot_kernels1, kernel1, padding='same', input_shape=(alto, largo, 1), activation='relu'))
cnn.add(MaxPooling2D(pool_size=stride))

# Capa 2
cnn.add(Convolution2D(tot_kernels2, kernel2, padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=stride))

# Capa 3
cnn.add(Convolution2D(tot_kernels3, kernel3, padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=stride))

cnn.add(Flatten())

# Capa totalmente conectada
cnn.add(Dense(256, activation='relu'))

# Aumento del dropout
cnn.add(Dropout(0.4))

# Capa de salida
cnn.add(Dense(clases, activation='softmax'))

cnn.compile(loss='categorical_crossentropy', optimizer=optimizers.Adam(learning_rate=lr), metrics=['accuracy'])

# Entrena el modelo
cnn.fit(imagen_entrenamiento, steps_per_epoch=pasos, epochs=epocas, validation_data=imagen_prueba, validation_steps=pasos_validacion)

# Guarda el modelo
dir = "./Parcial1/ConvolutionalNeuronal/modelo/"
if not os.path.exists(dir):
    os.mkdir(dir)

cnn.save(dir + 'modelo.keras')
cnn.save_weights(dir + 'pesos.weights.h5')
