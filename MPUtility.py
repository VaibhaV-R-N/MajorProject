import mediapipe as mp
import numpy as np
from keras.models import load_model

class Utility():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.Hands = self.mpHands.Hands(max_num_hands = 2)
        self.mpDraw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.startT2 = False
     
    def draw(self,img):
        self.img = img
        self.res = self.Hands.process(img)
        self.startT2 = True

        if self.res.multi_hand_landmarks and len(self.res.multi_hand_landmarks)  == 1:
            for hand in self.res.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(self.img,hand,self.mpHands.HAND_CONNECTIONS,self.mp_drawing_styles.get_default_hand_landmarks_style(),
                self.mp_drawing_styles.get_default_hand_connections_style())
        
        return self.img

    def predictGesture(self):
        try:
            if  self.res.multi_hand_landmarks  and len(self.res.multi_hand_landmarks)  == 1:
                data = []
                model = load_model('model.h5')
                data = [self.res.multi_hand_landmarks[0].landmark[i].x for i in range(21)]+[self.res.multi_hand_landmarks[0].landmark[i].y for i in range(21)]
                data = np.array(data).reshape(1,-1)
            
                return np.argmax(model.predict(data),axis=1)[0]
            
            elif  self.res.multi_hand_landmarks and len(self.res.multi_hand_landmarks)  == 2:
                return "exec"
        except Exception:
            pass
