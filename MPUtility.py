import mediapipe as mp
import numpy as np
import threading
from keras.models import load_model
from NotificationTaskHandler import NHandler

class Utility():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.nh = NHandler()
        self.Hands = self.mpHands.Hands(max_num_hands = 2)
        self.mpDraw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.startT2 = False
        self.created = False
        self.nh.AEnabled=True
        self.notificationEvent = threading.Event()
     
    def draw(self,img):
        self.img = img
        self.res = self.Hands.process(img)
        self.startT2 = True

        if self.res.multi_hand_landmarks and len(self.res.multi_hand_landmarks)  == 1:
            for hand in self.res.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(self.img,hand,self.mpHands.HAND_CONNECTIONS,self.mp_drawing_styles.get_default_hand_landmarks_style(),
                self.mp_drawing_styles.get_default_hand_connections_style())
        
        return self.img

    def isRightHand(self,res=None):
        if res:
            self.res = res
        if str(self.res.multi_handedness[0].classification[0].label) == "Left":
            if not self.notificationEvent.is_set():
                self.notificationEvent.set()
            return True
        if not self.created:
            threading.Thread(target=self.orientationNotification,args=["Invalid Hand!"]).start()
        return False 
    
    def isNotFlipped(self):
        wrist,mfTip = None,None
        landmarks = self.res.multi_hand_landmarks[0]
        wrist = landmarks.landmark[0].y
        mfTip = landmarks.landmark[12].y

        if mfTip < wrist:
            if not self.notificationEvent.is_set():
                self.notificationEvent.set()
            return True
        self.notificationEvent.clear()
        if not self.created:
            threading.Thread(target=self.orientationNotification,args=["Invalid Hand Orientation!"]).start()
        return False

    def orientationNotification(self,message):
        import time
        # self.notificationEvent.clear()
        self.created = True
        while True:
            self.nh.notify(title="Warning!",message=message)
            if self.notificationEvent.is_set():
                self.created = False
                self.notificationEvent.clear()
                break
            time.sleep(3)

    def predictGesture(self):
        try:
            if  self.res.multi_hand_landmarks  and (len(self.res.multi_hand_landmarks)  == 1) and self.isRightHand() and self.isNotFlipped():

                data = []
                model = load_model('model.h5')
                data = [self.res.multi_hand_landmarks[0].landmark[i].x for i in range(21)]+[self.res.multi_hand_landmarks[0].landmark[i].y for i in range(21)]
                data = np.array(data).reshape(1,-1)
                y_pred = model.predict(data)
                return int(np.argmax(y_pred,axis=1)[0])
            else:
                 
                return 0
        except Exception as e:
            pass
            # print(e)
    
    def getResult(self):
        return self.res