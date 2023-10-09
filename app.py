

from googletrans import Translator
from gtts import gTTS
import os
import playsound

# Solicita la frase y el idioma de destino
frase = input("Ingresa la frase que quieres traducir: ")
idioma_destino = input("Ingresa el idioma de destino (por ejemplo, 'es' para español): ")

# Crea una instancia del traductor y traduce la frase al idioma de destino
traductor = Translator()
traduccion = traductor.translate(frase, dest=idioma_destino)
frase_traducida = traduccion.text

# Crea una instancia de gTTS para generar el audio
tts = gTTS(text=frase_traducida, lang=idioma_destino)
tts.save("temp.wav")

# Reproduce el archivo de audio usando playsound
sound_file = "temp.wav"
playsound.playsound(sound_file)

