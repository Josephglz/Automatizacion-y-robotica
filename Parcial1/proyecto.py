import cv2
import numpy as np
from keras.api.utils import load_img, img_to_array
from keras.api.models import load_model

# Cargar el modelo y los pesos
modelo = "./Parcial1/ConvolutionalNeuronal/modelo/modelo.keras"
cnn = load_model(modelo)

alto, largo = 300, 300  # Tamaño de las imágenes para la predicción

def predict(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    image = cv2.resize(image, (alto, largo))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)  # Agregar dimensión adicional
    image = image / 255.0  # Normalizar la imagen
    arreglo = cnn.predict(image)
    return arreglo[0]  # Devuelve las probabilidades

# Nombres de las clases
clases = ['C1-GonzalezCabrales', 'C2-MonroyAguillon', 'C3-VargasLopez', 'C4-RamirezDelAngel']

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar la predicción
    probabilities = predict(frame)
    prediction_index = np.argmax(probabilities)
    confidence = probabilities[prediction_index]

    # Umbral de confianza
    if confidence < 0.5:  # Cambia el umbral si es necesario
        prediction_class = "Desconocido"
    else:
        prediction_class = clases[prediction_index]

    # Mostrar el resultado en la imagen
    cv2.putText(frame, f"{prediction_class} ({confidence:.2f})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar el frame con la predicción
    cv2.imshow('Detección de Personas', frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
