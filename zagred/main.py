import speech_recognition
import pyttsx3

class Receptor:
    def listen(self):
        microphone = speech_recognition.Recognizer()
        
        with speech_recognition.Microphone() as source:
            microphone.adjust_for_ambient_noise(source)
            audio = microphone.listen(source)
        
        try:
            print("Ouvindo... ")
            phrase = microphone.recognize_google(audio,language='pt-BR')
            self.__speak("Você disse: " + phrase)
        except: # speech_recognition.UnknownValueError
            self.__speak("Não entendi")
        
        return phrase


    def __speak(self, phrase):
        speaker = pyttsx3.init()
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[53].id)
        rate = speaker.getProperty('rate')
        speaker.setProperty('rate', rate-80)
        speaker.say(phrase)
        speaker.runAndWait()


if __name__ == '__main__':
    zagred = Receptor()
    zagred.listen()



