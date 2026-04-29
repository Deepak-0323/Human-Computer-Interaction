# Human-Computer-Interaction
Gesture-based touchless computer control system using MediaPipe and OpenCV.


# ✋ Air-Command: Gesture-Based Human-Computer Interaction System

Air-Command is a real-time, touchless Human-Computer Interaction (HCI) system that allows users to control a computer using hand gestures. The system uses computer vision and hand-tracking techniques to perform actions like slide navigation and volume control without any physical input device.

---

## 🚀 Features

* ✋ Real-time hand gesture detection
* ▶️ Slide navigation (Next / Previous)
* 🔊 Volume control using finger distance
* 🎥 Webcam-based interaction (no extra hardware required)
* ⚡ Fast and responsive performance

---

## 🧠 Technologies Used

* Python
* OpenCV – Video capture & processing
* MediaPipe – Hand tracking (21 landmarks)
* PyAutoGUI – System control automation
* NumPy – Mathematical operations

---

## ⚙️ How It Works

1. Webcam captures live video
2. OpenCV processes video frames
3. MediaPipe detects hand landmarks
4. Gesture logic identifies user actions
5. PyAutoGUI executes system commands

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Air-Command.git
cd Air-Command
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python air_command_project.py
```

---

## 🎯 Gesture Controls

| Gesture          | Action         |
| ---------------- | -------------- |
| ☝ 1 finger       | Next Slide     |
| ✌ 2 fingers      | Previous Slide |
| 🤏 Fingers far   | Volume Up      |
| 🤏 Fingers close | Volume Down    |

---

## 📌 Applications

* 📊 Presentation control
* 🏠 Smart home interaction
* ♿ Assistive technology
* 🖥 Touchless computing

---

## ⚠️ Limitations

* Performance depends on lighting conditions
* Requires clear hand visibility
* Accuracy may reduce in cluttered backgrounds

---

## 🔮 Future Enhancements

* 🖱 Hand-controlled mouse
* 🔊 On-screen volume indicator
* 🤖 AI-based gesture recognition
* 🌐 IoT device integration

---

## 📷 Demo

*(Add screenshots or demo video link here)*

---

## 👨‍💻 Author

Deepak Chawhan

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
