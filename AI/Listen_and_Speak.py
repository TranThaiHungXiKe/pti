import speech_recognition as sr
robot_ear = sr.Recognizer()
import pyttsx3

def text_to_speech(text:str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def speech_to_text()->str:
     try:
        with sr.Microphone()as mic:
            print("ROBOT:I'M listening ")

            audio = robot_ear.listen(mic,timeout=2 ,phrase_time_limit=2)

            text = robot_ear.recognize_google(audio)
            text = text.lower()
            text_to_speech("I Will Search For Food using keyboard : " + text)
            print(text)
            return text 
        
     except sr.UnknownValueError:
         text_to_speech("I Couldn't understand . Could you please repeat that ? ")
         return "" 

     except sr.RequestError as e:
        text_to_speech(f"Could not Request result from Google Speech Recognition service; {e}")
        return ""
