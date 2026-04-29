import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# volume control setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

# mediapipe setup
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()
    img = cv2.flip(img,1)

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

            h,w,c = img.shape

            x1 = int(handLms.landmark[4].x*w)   # thumb
            y1 = int(handLms.landmark[4].y*h)

            x2 = int(handLms.landmark[8].x*w)   # index
            y2 = int(handLms.landmark[8].y*h)

            cv2.circle(img,(x1,y1),10,(255,0,0),cv2.FILLED)
            cv2.circle(img,(x2,y2),10,(255,0,0),cv2.FILLED)

            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)

            length = np.hypot(x2-x1,y2-y1)

            # convert finger distance to volume
            vol = np.interp(length,[20,200],[minVol,maxVol])
            volume.SetMasterVolumeLevel(vol,None)

    cv2.imshow("Air Command Volume Control",img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()