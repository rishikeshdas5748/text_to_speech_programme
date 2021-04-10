from gtts import gTTS
import os

fh = "THIS IS A TEXT TO SPEECH TEST."

language = 'en'

output = gTTS(text=fh, lang=language, slow=False)

output.save('output.mp3')

os.system("start output.mp3")
