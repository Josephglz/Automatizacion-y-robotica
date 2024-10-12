
##modulos: SpeechRecognition  y PyAydio
# (en mac requiere-> 1) brew install portaudio  2) pip3 install pyaudio
import speech_recognition as sr

lista = sr.Microphone.list_microphone_names()

for index, name in enumerate(lista):
    print(index, " - ", name)




