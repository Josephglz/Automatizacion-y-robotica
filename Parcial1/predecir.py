import os
import numpy as np
from keras.api.utils import load_img, img_to_array
from keras.api.models import load_model

alto, largo = 300, 300
modelo = "./Parcial1/ConvolutionalNeuronal/modelo/modelo.keras"
pesos = './Parcial1/ConvolutionalNeuronal/modelo/pesos.weights.h5'

cnn = load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
    imagen_a_predecir = load_img(file, target_size=(alto, largo), color_mode="grayscale")
    imagen_a_predecir = img_to_array(imagen_a_predecir) / 255.0
    imagen_a_predecir = np.expand_dims(imagen_a_predecir, axis=0)
    
    arreglo = cnn.predict(imagen_a_predecir)
    # print(f'Predicción numérica: {arreglo}')  # Agregado para depuración
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)
    
    match respuesta:
        case 0:
            return 'C1-GonzalezCabrales'
        case 1:
            return 'C2-MonroyAguillon'
        case 2:
            return 'C3-VargasLopez'
        case 3:
            return 'C4-RamirezDelAngel'
        case _:
            return '----'


def get_folders_name_from(from_location):
    return sorted([folder for folder in os.listdir(from_location) if os.path.isdir(os.path.join(from_location, folder))])

def probar_red_neuronal():
    base_location = "./Parcial1/ConvolutionalNeuronal/F3-Prueba/"
    folders = get_folders_name_from(base_location)

    correct = {folder: 0 for folder in folders}  # Diccionario para contar aciertos por clase
    total_predictions = {folder: 0 for folder in folders}  # Diccionario para contar predicciones por clase

    for folder in folders:
        files = [archivo for archivo in os.listdir(os.path.join(base_location, folder)) 
                 if archivo.endswith((".jpg", ".jpeg", ".png"))]
        
        for file in files:
            composed_location = os.path.join(base_location, folder, file)
            prediction = predict(composed_location)
            print(f'Comparando: {folder} | Evaluando: Clase {folder} / {file} | PREDICCIÓN: {prediction}')
            
            total_predictions[folder] += 1
            
            if prediction.startswith(folder):
                correct[folder] += 1

    # Calcular y mostrar la eficiencia de cada clase y la eficiencia total
    total_correct = sum(correct.values())
    total_count = sum(total_predictions.values())

    for folder in folders:
        if total_predictions[folder] > 0:
            class_accuracy = (correct[folder] / total_predictions[folder]) * 100
            print(f'Eficiencia de {folder}: {class_accuracy:.2f}%')
    
    overall_efficiency = (total_correct / total_count) * 100 if total_count > 0 else 0
    print(f'Eficiencia total de la red: {overall_efficiency:.2f}%')

probar_red_neuronal()
