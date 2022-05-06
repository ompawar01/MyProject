import pyttsx3
import datetime
import wikipedia
import pyaudio
import webbrowser
import sys
import smtplib
import pyjokes
import operator
import pyautogui
import instaloader
import speech_recognition as sr
from PyQt5 import QtWidgets , QtCore ,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis.JarvisUI2 import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
#print(voices[1].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am System Sir.Please tell me how may I help you")

class MainThread(QThread):
    def _init_(self):
        super(MainThread, self)._init_()


    def run(self):
        self.TaskExecution(self) 

    def takeCommand(self):
    #It takes microphone input from the user and return string output

        r = sr.Recognizer() #it helps us to recognize audio
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete   bolanyat gap ala tar to gap 1 second cha consider karayacha
            audio = r.listen(source,timeout=2,phrase_time_limit=5)



        try:
            print("Recognizing...") 
            
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
        return query
  
    def TaskExecution(self) :
        # if _name_ == 'main':
            speak("hey friend")
            WishMe()
            while True: 
                self.query =self.takeCommand().lower()

                #Logic for executing tasks based on query
                
                
                if 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query,sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'taj mahal' in self.query:
                    speak('According to unesco taj mahal is an immense mausoleum of white marble, built in Agra between 1631 and 1648 by order of the Mughal emperor Shah Jahan in memory of his favourite wife, the Taj Mahal is the jewel of Muslim art in India and one of the universally admired masterpieces of the world heritage.')
                elif 'built' in self.query:
                    speak('The Taj Mahal was built Agra between 1631 and 1648 by the Mughal emperor to immortalize his wife Mumtaz Mahal  who died in childbirth in 1631, having been the emperor’s inseparable companion since their marriage in 1612. ')
                elif 'where'in self.query:
                    speak('Taj mahal is located in Agra city of India')
                elif 'height' in self.query:
                    speak('The height of taj mahal is seventy three meters which is two hundred and forty feet')
                elif 'area' in self.query:
                    speak('The area of taj mahal is seventeen hectares')
                elif 'youtube' in self.query:  
                    webbrowser.open('youtube.com')
                elif 'google' in self.query:
                    webbrowser.open('google.com')
                elif 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S:%DD:%MM:%YYYY")

startExecution = MainThread()

class Main(QMainWindow):
    def _init_(self):
        super()._init_()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton.clicked.connect(self.showTime)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/Coding_Ninjas_Java_With_DSA/67397826-bienvenido-a-la-india-con-la-ilustración-del-cartel-famosa-atracción-de-vectores-el-diseño-del-recor.webp")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

    
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())