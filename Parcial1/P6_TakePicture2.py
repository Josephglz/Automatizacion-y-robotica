import time
import cv2  # opencv
import os


def takepicture(integrante):

    cam = cv2.VideoCapture(0)  # videocámara
    tiempo_inicial = time.time()  # Guardar el tiempo inicial
    contFotos = 0
    folder = "./integrante_" + integrante
    if not os.path.exists(folder):
        os.makedirs(folder)

    while contFotos < 175:
        result, image = cam.read()
        if result:
            cv2.imshow("Camara_Principal", image)
            res = cv2.waitKey(1)

            tiempo_actual = time.time()
            if tiempo_actual - tiempo_inicial >= 1:
                cv2.imwrite("./integrante_" + integrante + "/foto_" + str(contFotos) + ".png", image)
                contFotos += 1
                tiempo_inicial = tiempo_actual

            if res == ord("q"):
                cam.release()
                cv2.destroyWindow("Camara_Principal")
                break

        else:
            print("No image detected. Please try again.")
            break

if __name__ == "__main__":
    integrantes = 4
    for i in range(integrantes):
        takepicture(str(i + 1))
        time.sleep(5)