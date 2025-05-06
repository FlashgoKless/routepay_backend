import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Пожалуйста, говорите...")
    
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        audio = recognizer.listen(source)
        
        print("Обработка вашего голоса...")
        
        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            return(text)
            
        except sr.UnknownValueError:
            return("Извините, я не смог распознать вашу речь")
        except sr.RequestError as e:
            return(f"Ошибка сервиса распознавания; {e}")

if __name__ == "__main__":
    print(recognize_speech_from_mic())
