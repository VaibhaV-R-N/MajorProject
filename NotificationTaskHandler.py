import platform
import subprocess
from plyer import notification

class NHandler:
    def __init__(self):
        self.OS = platform.system()

    def notify(self,message,title="Gesture",duration=1):
        if self.OS == "Linux" and message != None:
            subprocess.run(["notify-send", "-t", str(duration),message])
        elif self.OS == "Windows":
            notification.notify(title=title,message=message)
    
    def exe(self,task):
        subprocess.run(task)

# def __main__():
#     h = handler()
#     h.sendNotification("hi")

# __main__()
