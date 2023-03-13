import cv2 as cv
import math

from HandState import tip,base
w,h = [ 638,478]


def drawCircle(center,img):
    cv.circle(img,center,3,(255,0,0),3)
    return img
    

def giveCenter(landmarks,i,part):
    # print(w,h)
    return (math.floor((landmarks.landmark[part[i]].x)*w),math.floor((landmarks.landmark[part[i]].y)*h))


def draw(res,img):
    if res.multi_hand_landmarks and len(res.multi_hand_landmarks) == 1:
        for landmarks in res.multi_hand_landmarks:
            for i in range(5):
                center = giveCenter(landmarks,i,tip)
                # print(center)
                img = drawCircle(center,img)
            for i in range(1,5):
                center = giveCenter(landmarks,i,base)
                img = drawCircle(center,img)
    return img

