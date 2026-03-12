from gtts import gTTS

def speak_telugu(text, output_file="response.mp3"):
    tts = gTTS(text=text, lang='te')
    tts.save(output_file)
    return output_file
