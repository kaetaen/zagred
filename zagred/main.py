from urllib import parse
import speech_recognition
import pyttsx3
import re
import os

class Receptor:
    def listen(self):
        microphone = speech_recognition.Recognizer()
        phrase = ''

        with speech_recognition.Microphone() as source:
            microphone.adjust_for_ambient_noise(source)
            audio = microphone.listen(source)
        
        try:
            print("Ouvindo... ")
            phrase = microphone.recognize_google(audio,language='pt-BR')
            self.__speak("Você disse: " + phrase)
        except: # speech_recognition.UnknownValueError
            self.__speak("Não entendi")
        if (phrase):
            return phrase


    def __speak(self, phrase):
        speaker = pyttsx3.init()
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[53].id)
        rate = speaker.getProperty('rate')
        speaker.setProperty('rate', rate-80)
        speaker.say(phrase)
        speaker.runAndWait()


class CommandRunner(Receptor):
    def __init__(self):
        self.__command = self.listen()

    def exec_command(self):
        command = self.__command    
        parsed_voice_command = re.search('print*', command)
        if (parsed_voice_command):
            os.system('xfce4-screenshooter -f -s .')

    
    def __command_parser(self): 
        ...

if __name__ == '__main__':
    zagred = CommandRunner()
    zagred.exec_command()



