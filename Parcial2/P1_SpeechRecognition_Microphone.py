import speech_recognition as sr
r = sr.Recognizer()
print("Inicia:")
with sr.Microphone() as source:
    # r.adjust_for_ambient_noise(source, duration=0.5)  # Ajusta el ruido ambiental por 0.5 segundos
    # audio = r.listen(source)
    r.adjust_for_ambient_noise(source) # listen for 1 second
    audio = r.listen(source)


print("Registro Generado!")

try:
    cadena =  r.recognize_google(audio, language="es-MX")
    print("Mensaje: " + cadena)
    cadena = cadena.lower()

    if "puerta" in cadena:
        if "abrir" in cadena:
            print("Abriendo Puerta")
        elif "cerrar" in cadena:
            print("Cerrando Puerta")
        else:
            print("No se reconoce la instrucción para la puerta")
    if "luz" in cadena:
        if "encender" in cadena:
            print("Encendiendo Luz")
        elif "apagar" in cadena:
            print("Apagando Luz")
        else:
            print("No se reconoce la instrucción para la luz")
    else:
        print("Instrucción no registrada. Dijiste: " + cadena)

except sr.UnknownValueError:
    print("Unknown Value Error")
except sr.RequestError as e:
    print("Request Error: ".format(e))
except Exception as ex:
    print("Error: ".format(ex))
