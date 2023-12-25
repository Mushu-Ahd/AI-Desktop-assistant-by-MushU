import smtplib
import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import webbrowser
import os
import sys




def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 4:
        speak("It's so mid night, isn't it?")

    elif hour >= 4 and hour <12:
        speak("Morning Mushu. I'm sure you are having a great day...")

    elif hour >=12 and hour < 18:
        speak('Good Afternoon Mushu')
    
    else:
        speak("Good evening Mushu")
    speak("Myself Alfred , how may i help you Today?")
def open_file(folder, filename):
    file_path = os.path.join(folder, filename)
    try:
        os.startfile(file_path)
        print(f"Opened {filename}")
    except Exception as e:
        print(f"Error: {e}")

# Function to edit the name of a file
def edit_file_name(folder, old_filename, new_filename):
    old_path = os.path.join(folder, old_filename)
    new_path = os.path.join(folder, new_filename)
    try:
        os.rename(old_path, new_path)
        print(f"Renamed {old_filename} to {new_filename}")
    except Exception as e:
        print(f"Error: {e}")

# Function to create a new file
def create_file(folder, filename):
    file_path = os.path.join(folder, filename)
    try:
        with open(file_path, 'w') as file:
            file.write('')
        print(f"Created {filename}")
    except Exception as e:
        print(f"Error: {e}")

# Function to move a file
def move_file(source_folder, target_folder, filename):
    source_path = os.path.join(source_folder, filename)
    target_path = os.path.join(target_folder, filename)
    try:
        os.rename(source_path, target_path)
        print(f"Moved {filename} to {target_folder}")
    except Exception as e:
        print(f"Error: {e}")

# Function to delete a file
def delete_file(folder, filename):
    file_path = os.path.join(folder, filename)
    try:
        os.remove(file_path)
        print(f"Deleted {filename}")
    except Exception as e:
        print(f"Error: {e}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing what you said...")
        query = r.recognize_google(audio , language='en-in')
        print("User said: " , query)

    except Exception as e:
        #print(e)
        speak("can you say that again please...")
        return "None"
    return query


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)

    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.echo()
    server.starttls()
    server.login('mushuahd@gmail.com', 'ShaikhMushuAhd.8080')
    server.sendmail('mushuahd@gmail.com', to , content)
    server.close()

if __name__ == "__main__":

    wishMe()
    #while True:

    def function():

        lst = ["Search on Internet", "Open Brower" , "StackOverFlow" , "Current Time" , "Open Code" , "Play Games"]


        query = takeCommand().lower()

        if 'search on internet'.lower() in query:
            speak('Searching on internet'.lower())
            query = query.replace("searching on internet" , "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to my sources of knowledge and the data internet has...")
            print(results)
            speak(results)

        elif 'open browser'.lower() in query :
            speak("can you specify, which site do you want to open or visit?")
            output = takeCommand()
            if "youtube".lower() in output:
                webbrowser.open("youtube.com")
            elif "instagram".lower() in output:
                webbrowser.open("instagram.com")
                
            elif "facebook".lower() in output:
                webbrowser.open("facebook.com")
                
            elif "spotify".lower() in output:
                webbrowser.open("spotify.com")
                
            elif "google".lower() in output:
                webbrowser.open("google.com")

            
            else:
                speak(f"sorry, i don't know much about {output} website. so i am gonna open Google search engine. you may search on it...")
                webbrowser.open("google.com")

        elif 'stackoverflow'.lower() in query :
            webbrowser.open("stackoverflow.com")

        elif "current time".lower() in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"According to this system timing, the current time is {strTime}")
            
        elif "open code".lower() in query:
            path = "C:\\Users\\musha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "send email".lower() in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'mushuahd@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent...")
            
            except Exception as e:
                print(e)
                speak("sorry bro, the email hasn't sent...")

        elif "open drive".lower() in query:
            speak("can you specify which folder do you want to open in This pc?")
            file = takeCommand()
            if f"first drive".lower() in file.lower():
                speak("Opening c drive...")
                os.startfile("c:\\")
            
            elif f"second drive".lower() in file.lower():
                speak("Opening d drive...")
                os.startfile("d:\\")
            
        elif "play game".lower() in query:
            speak(" Ok but which game, can you specify please...")
            game = takeCommand()
            if "car" in game:
                path = "D:\\Froza Horizon 4\\Forza.Horizon.4(GamingBeasts.com)\\Forza.Horizon.4.v1.476.400.0.Incl.ALL.DLC\\Forza.Horizon.4.v1.476.400.0.Incl.ALL.DLC\\ForzaHorizon4.exe"
                speak("alright sir, The game is about to start.")
                os.startfile(path)

            elif "GTA 5".lower() in game:
                path = ""
                speak("Ok master, The game is about to start. please make sure you have connected the external keyboard and mouse along with charging cable for better experience...")
            
            else:
                speak("sorry sir, their is only one game in this device right")


        elif "friend".lower() in query:
            
            speak("can you specify more, means your friend name?")
            
            frd = takeCommand()
            
            if "wasef" and "wasif" in frd.lower():
                speak("wasif, one of your B.C.S. batchmate. According to my knowledge, he is the finest friend of yours. He lives in the area called Kat-kat gate. He is also a gym-rat, but currently he turned out to be gay. LGBTQ supporter.  ")
                print(speak)

            else:
                pass

        elif "close the program".lower() in query:
            
            speak('are you sure?')
            
            sen = takeCommand()
            
            if 'yes' in sen :
                speak("alright sir, thanks for having me as your assistant")
                sys.exit(0)
            
            elif 'no' in sen:
                speak("what can i do for you ?")
                cmd = takeCommand()
                function()
            
            else:
                pass
        
        elif "open pdf" in query:
            
            speak("which PDF do you want to open? Can you specify.. please")
            
            pf = takeCommand().lower()

            if "machine learning".lower() in pf:

                speak("opening Machine learning PDF, please wait...")

                path = "D:\\Hands on Machine Learning.pdf"

                os.startfile(path)
            
            else:
                #pass for now...
                pass 
        
        elif 'perform task on file' in query:
            if "open file" in query:
                folder = "D:\\"                               # Specify the folder path
                filename = query.replace("open file", "").strip()
                open_file(folder, filename)

            elif "edit file" in query:
                folder = "D:\\"                               # Specify the folder path
                parts = query.replace("edit file", "").strip().split(" to ")
                old_filename, new_filename = parts[0], parts[1]
                edit_file_name(folder, old_filename, new_filename)
                
            elif "create file" in query:
                folder = "D:\\"                               # Specify the folder path
                filename = query.replace("create file", "").strip()
                create_file(folder, filename)
                
            elif "move file" in query:
                source_folder = "D:\\"                       # Specify the source folder path
                target_folder = "D:\\"                       # Specify the target folder path
                filename = query.replace("move file", "").strip()
                move_file(source_folder, target_folder, filename)

            elif "delete file" in query:
                folder = "D:\\"                             # Specify the folder path
                filename = query.replace("delete file", "").strip()
                delete_file(folder, filename)
            elif "exit" in query:
                speak("sorry... please try again. I didn't get you")

        
    function()
