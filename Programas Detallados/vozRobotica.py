import speech_recognition as spr
from gtts import gTTS
import os

voz = ""

while True:
    reconocedor = spr.Recognizer()
    with spr.Microphone() as fuente:
        try:
            audio = reconocedor.listen(fuente)
            texto = reconocedor.recognize_google(audio)
            print(texto)

            if texto == "detener":
                break
            texto = reconocedor.recognize_google(audio)
            voz += str(texto)
        except:
            print("Diga Algo...")

hr = gTTS(text=voz, lang="es", slow=False)
hr.save("prueba.wav")