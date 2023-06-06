from tkinter import *
import sys

top = Tk()
top.geometry("400x400")
c=Canvas(top,bg="green",height=200,width=200)
fname=PhotoImage(file="C:\\Users\\anees ahmed siddiqui\\Downloads\\SEM_IV(56,36,09,102)\\SEM_IV(56,36,09,102)\\jjjj1.png")
b_label=Label(top,image=fname)
b_label.place(x=0,y=0,relwidth=1,relheight=1)

def ret():
    top.destroy()
    print("I am gone, restart me!!!")

def start():
    import pyttsx3 #text to speech
    import speech_recognition as sr 
    import datetime #for datetime
    import wikipedia #for wikipedia
    import webbrowser #for opening websites
    import os #operating system
    import smtplib #
    import sys
    
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    print(voices[0].id)
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-40)

      


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Good Morning!")
            speak('Good Morning!')
        elif  hour>=12 and hour<18:
            print("Good Afternoon!")
            speak("Good Afternoon!")
        else:
            print("Good Evening!")
            speak('Good Evening!')

        print("I am Your Voice Assistant, how can I help You!")
        speak('I am Your Voice Assistant, how can I help You!')

    def takeCommand(): #it takes microphone input from the user and return string output
        r=sr.Recognizer()
        with sr.Microphone() as source:  # use the default microphone as the audio source
            print("Tell me i am Listening....")
            r.pause_threshold=0.5
            audio=r.listen(source)  # listen for the first phrase and extract it into audio data
        try:
            print("Please wait for recognition...")
            query=r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")

        except Exception as e:
            print(e)

            print("I can't Listen Please Say That Again.....")
            return "None"
        return query
    
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('beepractice1@gmail.com', 'BeePract@001')
        server.sendmail('james2420bond@gmail.com',to, content)
        server.close()

    if __name__=='__main__':
        #speak('Hassam')
        wishMe()
        while True:
        #if 1:
            query = takeCommand().lower() #Logic for executing task
            if  'wikipedia' in query:
                speak('Searching Wikipedia....')
                query=query.replace("wikipedia","")
                result=wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            
            elif 'youtube' in query:
                webbrowser.open("youtube.com")

            elif 'google' in query:
                webbrowser.open("google.com")

            elif 'stack overflow' in query:
                webbrowser.open("stackoverflow.com")
                
            elif 'ipl score table' in query:
                webbrowser.open("outlookindia.com/ipl/pointtable")
                
            elif "today's weather" in query:
                webbrowser.open("shorturl.at/npFM2")




            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
                print(strTime)
           
            elif 'date' in query:
                strDate=datetime.date.today()
                print(strDate.day,strDate.month,strDate.year)
                speak("today date is {strDate}")
                print(strDate)

            elif 'chrome' in query:
                codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)

            elif 'play music' in query:
                music_dir = 'C:\\Users\\anees ahmed siddiqui\\Music'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'email' in query:
                try:
                    print('What conversation you want to say Please tell me?')
                    speak('What conversation you want to say Please tell me?')
                    content = takeCommand()
                    to="james2420bond@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                    print("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")

            
            elif "close yourself" in query:
                sys.exit(0)
            elif "exit" in query:
                sys.exit(0)

            elif 'your name' in query:
                speak('I am Voice Assistant Made By The student of KVMIT')
                print("I am Voice Assistant Made By The student of kvmit")

            elif 'how are you' in query:
                speak("I am fine. What about yourself?")
                print("I am fine. What about yourself?")


               
name = Label(top, text = "THIS IS OUR GUI BASED VOICE ASSISTANT.")
name.place(x = 100,y = 130)
b1 = Button(top,text = "Tap to Give Commands",command = start)
b1.place(x = 145, y = 175)
b2 = Button(top,text = "CLOSE ME!!!",bg="red",foreground="#FFFFFF",command = ret)
b2.place(x = 175, y = 220)
c.pack()
top.mainloop()    
