import csv
import cv2 as cv
import mediapipe as mp
from pynput import keyboard


global results
filename = "landmarkDataset.csv"

def writeToDataset(key):
    try:
        with open(filename,"a") as file:
            writer = csv.writer(file)

            if key.char == '1':
                 writer.writerow([results.multi_hand_landmarks[0].landmark[i].x for i in range(21)]+[results.multi_hand_landmarks[0].landmark[i].y for i in range(21)]+[1])
            if key.char == '2':
               writer.writerow([results.multi_hand_landmarks[0].landmark[i].x for i in range(21)]+[results.multi_hand_landmarks[0].landmark[i].y for i in range(21)]+[2])
            if key.char == '3':
                writer.writerow([results.multi_hand_landmarks[0].landmark[i].x for i in range(21)]+[results.multi_hand_landmarks[0].landmark[i].y for i in range(21)]+[3])
            if key.char == '4':
                writer.writerow([results.multi_hand_landmarks[0].landmark[i].x for i in range(21)]+[results.multi_hand_landmarks[0].landmark[i].y for i in range(21)]+[4])
            if key.char == '5':
                writer.writerow([results.multi_hand_landmarks[0].landmark[i].x for i in range(21)]+[results.multi_hand_landmarks[0].landmark[i].y for i in range(21)]+[5])
            if key.char == '6':
                writer.writerow([results.multi_hand_landmarks[0].landmark[i].x for i in range(21)]+[results.multi_hand_landmarks[0].landmark[i].y for i in range(21)]+[6])
    except Exception:
        print("error")
        pass

listener = keyboard.Listener(on_press=writeToDataset)
listener.start()



fields = []

videoSrc = cv.VideoCapture(0)

cv.namedWindow("videoCam",cv.WINDOW_NORMAL)

mpHands = mp.solutions.hands
Hands = mpHands.Hands(max_num_hands = 1)
mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# fields = [f'{mpHands.HandLandmark(i).name}_x' for i in range(21)] + [f'{mpHands.HandLandmark(i).name}_y' for i in range(21)]
# fields.append("class")
# print(fields)

# with open(filename,'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(fields)

while True:
    _,img = videoSrc.read()

    img = cv.flip(img,1)
    results = Hands.process(img)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(img,landmarks,mpHands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    cv.imshow("videoCam",img)


    if cv.waitKey(1) & 0xFF == ord('x'):
        cv.destroyAllWindows()
        exit(0)
      



