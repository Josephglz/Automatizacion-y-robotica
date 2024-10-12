import time
import cv2  ##opencv
cam = cv2.VideoCapture(0) ##videocamara ---
contFotos = 0
while True:
    result, image = cam.read()
    if result:
        cv2.imshow("Camara_Principal", image)
        res = cv2.waitKey(1) ## 1  = .. no detenga la ejecucion
        #print(res , "  ", ord("q"))
        if res == ord("q"):
            cam.release()
            cv2.destroyWindow("Camara_Principal")
            break
        elif res == ord(" "): ##space
            cv2.imwrite("foto_"+ str(contFotos) +".png", image)
            contFotos+=1

    else:
        print("No image detected. Please! try again")
        break