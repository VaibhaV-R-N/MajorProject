 #tip = 4 8 12 16 20
tip = [4,8,12,16,20]
#base = 5 5 9 13 17
base = [5,5,9,13,17]
from MPUtility import Utility
mpu = Utility()

def getState(res):
    handState = [0,0,0,0,0]
   
    if res.multi_hand_landmarks and (len(res.multi_hand_landmarks ) == 1) and mpu.isRightHand() and mpu.isNotFlipped() :
        for landmarks in res.multi_hand_landmarks:
            if landmarks.landmark[tip[0]].x > landmarks.landmark[base[0]].x:
                handState[0] = 1
            for i in range(1,5):
                if landmarks.landmark[tip[i]].y < landmarks.landmark[base[i]].y:
                    handState[i] = 1
    return handState


def stateToGesture(handState):
    gesture = 0
    cont = True
    for i in range(1,5):
        if handState[i] == 1 and cont:
            gesture += 1
        if handState[i] == 0 and cont:
            cont = False
        if handState[i] == 1 and cont == False:
            return 0
            
    if gesture != 4 and handState[0] == 1:
        return 0
    if gesture == 4 and handState[0] == 1:
        gesture+=1
    return gesture
            