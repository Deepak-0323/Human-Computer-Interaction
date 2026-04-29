import pyautogui

print("AIR COMMAND - Gesture Simulation")
print("Press keys to simulate gestures")
print("L = Left Gesture")
print("R = Right Gesture")
print("U = Volume Up")
print("D = Volume Down")
print("Q = Quit")

while True:

    gesture = input("Enter Gesture: ").lower()

    if gesture == "l":
        print("Left Gesture Detected")
        pyautogui.press("left")

    elif gesture == "r":
        print("Right Gesture Detected")
        pyautogui.press("right")

    elif gesture == "u":
        print("Volume Up")
        pyautogui.press("volumeup")

    elif gesture == "d":
        print("Volume Down")
        pyautogui.press("volumedown")

    elif gesture == "q":
        print("Exiting program")
        break

    else:
        print("Unknown gesture")