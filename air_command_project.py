import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

pyautogui.FAILSAFE = False

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)

mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

gesture = "NONE"
last_action_time = 0

cv2.namedWindow("Air Command System", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Air Command System", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:

    success,img = cap.read()

    if not success:
        break

    img = cv2.flip(img,1)

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

            h,w,c = img.shape

            thumb_x = int(handLms.landmark[4].x*w)
            thumb_y = int(handLms.landmark[4].y*h)

            index_x = int(handLms.landmark[8].x*w)
            index_y = int(handLms.landmark[8].y*h)

            index_tip = handLms.landmark[8].y
            index_base = handLms.landmark[6].y

            middle_tip = handLms.landmark[12].y
            middle_base = handLms.landmark[10].y

            current_time = time.time()

            distance = np.hypot(index_x-thumb_x,index_y-thumb_y)

            # -------- VOLUME UP --------
            if distance > 180:

                gesture = "VOLUME UP"

                if current_time-last_action_time > 0.8:
                    pyautogui.press("volumeup")
                    last_action_time = current_time


            # -------- VOLUME DOWN --------
            elif distance < 40:

                gesture = "VOLUME DOWN"

                if current_time-last_action_time > 0.8:
                    pyautogui.press("volumedown")
                    last_action_time = current_time


            # -------- NEXT SLIDE --------
            elif index_tip < index_base and middle_tip > middle_base:

                gesture = "NEXT SLIDE"

                if current_time-last_action_time > 1:
                    pyautogui.press("right")
                    last_action_time = current_time


            # -------- PREVIOUS SLIDE --------
            elif index_tip < index_base and middle_tip < middle_base:

                gesture = "PREVIOUS SLIDE"

                if current_time-last_action_time > 1:
                    pyautogui.press("left")
                    last_action_time = current_time


            cv2.circle(img,(thumb_x,thumb_y),10,(255,0,0),cv2.FILLED)
            cv2.circle(img,(index_x,index_y),10,(255,0,0),cv2.FILLED)

            cv2.line(img,(thumb_x,thumb_y),(index_x,index_y),(0,255,0),3)

    else:
        gesture = "NO HAND"

    cv2.putText(img,gesture,(40,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,(0,255,0),4)

    cv2.imshow("Air Command System",img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()