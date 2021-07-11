import speech_recognition
import pyttsx3

def get_audio():
    microphone = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microphone.listen(source)
    
    try:
        phrase = microphone.recognize_google(audio,language='pt-BR')
        print("Você disse: " + phrase)
    except speech_recognition.UnkownValueError:
        print("Não entendi")
    
    return frase


def talk(phrase):
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[53].id)
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate-80)
    speaker.say(phrase)
    speaker.runAndWait()


