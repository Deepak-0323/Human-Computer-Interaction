import cv2
import mediapipe as mp
import pyautogui
import time

pyautogui.FAILSAFE = False

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

gesture = "None"
last_action_time = 0

while True:

    success, img = cap.read()
    img = cv2.flip(img,1)

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            index_tip = handLms.landmark[8].y
            middle_tip = handLms.landmark[12].y

            index_base = handLms.landmark[6].y
            middle_base = handLms.landmark[10].y

            current_time = time.time()

            # ONE FINGER → NEXT SLIDE
            if index_tip < index_base and middle_tip > middle_base:

                gesture = "NEXT SLIDE"

                if current_time - last_action_time > 1:
                    pyautogui.press("right")
                    last_action_time = current_time

            # TWO FINGERS → PREVIOUS SLIDE
            elif index_tip < index_base and middle_tip < middle_base:

                gesture = "PREVIOUS SLIDE"

                if current_time - last_action_time > 1:
                    pyautogui.press("left")
                    last_action_time = current_time

            else:
                gesture = "HAND DETECTED"

    else:
        gesture = "NO HAND"

    cv2.putText(img, gesture, (20,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0,255,0), 3)

    cv2.imshow("Air Command Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()