import platform
import subprocess
from plyer import notification
import pyttsx3
import threading
class NHandler:
    def __init__(self):
        self.OS = platform.system()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate',150)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice','English (America, New York City)')
        self.AEnabled = False
        self.NEnabled = True

    def voiceNotification(self,message):
        try:
            if self.AEnabled:
                self.engine.say(message)
                self.engine.runAndWait()
        except Exception as e:
            pass
            # print(e)

    def notify(self,message,title="Gesture",duration=1):
        if (self.OS == "Linux") and (message != None):
            if self.NEnabled:
                subprocess.run(["notify-send", "-t", str(duration),message])
            threading.Thread(target=self.voiceNotification,args=[message]).start()

        if (self.OS == "Windows") and (message != None):
            if self.NEnabled:
                notification.notify(title=title,message=message)
            threading.Thread(target=self.voiceNotification,args=[message]).start()
    
    def exe(self,task):
        subprocess.run(task)
        self.notify(title='task',message='completed!!',duration=10)

# def __main__():
#     h = NHandler()
#     for v in h.voices:
#         print(v)

# __main__()
