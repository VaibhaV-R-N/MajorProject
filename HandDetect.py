import cv2 as cv
import mediapipe as mp
import HandState as hs
import LandMarks as lms
import GestureFilter as gesf
from threading import Thread

mpHands = mp.solutions.hands
Hands = mpHands.Hands(max_num_hands = 2)

w,h = [480,360]

gf = gesf.GestureFilter()

vidSrc = cv.VideoCapture(0)
cv.namedWindow("videoCam",cv.WINDOW_NORMAL)
t2 = Thread(target=gf.filter)
t2.start()
t3 = Thread(target=gf.getValue)
t3.start()

while True:
    _,img = vidSrc.read()
    cv.resizeWindow("videoCam",w,h)
    cv.flip(img,1)
    cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result = Hands.process(img)

    #using HandState module
    state = hs.getState(result)
    # print(state)
    gesture = hs.stateToGesture(state)
    t1 = Thread(target=gf.gestureUpdater,args=[gesture])
   
    t1.start()
   
    img = lms.draw(result,img)
   
    cv.imshow("videoCam",img)
    t1.join()

    if cv.waitKey(2) & 0xFF==ord('x'):
        cv.destroyAllWindows()
        break




