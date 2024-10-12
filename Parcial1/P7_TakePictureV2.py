import time
import cv2
import os

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def face_detect_box(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    faces_frames = []
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)
        aux = image.copy()
        faces_frames.append(aux[y:y+h, x:x+w])

    return faces, faces_frames

def takepicture(integrante):
    cam = cv2.VideoCapture(0)  # videocámara
    tiempo_inicial = time.time()  # Guardar el tiempo inicial
    contFotos = 0
    folder = "./Pictures/integrante_" + integrante
    if not os.path.exists(folder):
        os.makedirs(folder)

    while contFotos < 175:
        result, image = cam.read()
        if result:
            faces_detected, img_faces = face_detect_box(image)
            cv2.imshow("Camara_Principal", image)

            res = cv2.waitKey(1)
            if res == ord("q"):
                cam.release()
                cv2.destroyWindow("Camara_Principal")
                break
            
            tiempo_actual = time.time()
            if tiempo_actual - tiempo_inicial >= 1:
                if len(img_faces) == 0:
                    cv2.imwrite("./Pictures/integrante_" + integrante + "/foto_" + str(contFotos) + ".png", image)
                else:
                    imagen_cara = cv2.resize(img_faces[0], (300, 300), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite("./Pictures/integrante_" + integrante + "/foto_" + str(contFotos) +  ".png", imagen_cara)
                contFotos += 1
                tiempo_inicial = tiempo_actual
        else:
            print("No image detected. Please try again.")
            break


if __name__ == "__main__":
    integrantes = 4
    for i in range(integrantes):
        print("Tomando fotos integrante " + str(i + 1))
        takepicture(str(i + 1))
        time.sleep(10)