import speech_recognition as s
#create a object of Recognizer
sr=s.Recognizer()
print("i am listening you.........")
with s.Microphone() as m:
    try:
        audio=sr.listen(m)
        query=sr.recognize_google(audio,language='eng-in')
        print(query+".")
    except:
        print("Sorry, I could not recognize what you said.")

