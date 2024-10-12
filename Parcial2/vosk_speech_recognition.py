import sys
import os
from vosk import Model, KaldiRecognizer
import pyaudio

path = './Parcial2/model'

# Load the Vosk model
if not os.path.exists(path):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    sys.exit(1)

model = Model(path)
recognizer = KaldiRecognizer(model, 16000)

# Start audio stream
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Listening...")

while True:
    data = stream.read(4000)
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        print(result)
    else:
        pass
        # partial_result = recognizer.PartialResult()
        # print(partial_result)