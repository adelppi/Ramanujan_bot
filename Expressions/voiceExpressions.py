from gtts import gTTS

def statement2mp3(statement):
    gTTS(statement, lang = "ja").save("./voices/voice.mp3")