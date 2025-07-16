# ⏳ Countdown Timer
A versatile desktop countdown timer application built with Python. It features a settings window to specify the duration and a separate display window with full controls for the countdown. The interface is built with PyQt5, and it uses Pygame for the final sound notification.

<br>

## ✨ Features

- **Custom Duration:** Set a countdown timer using intuitive dropdowns for hours, minutes, and seconds.
- **Separate Display Window:** The timer runs in a second, dedicated window, keeping the interface clean.
- **Pause & Resume:** Easily pause and resume the countdown at any time using the "Pause/Resume" button.
- **Reset Functionality:** Reset the timer back to its initial duration with a single click on the "Reset" button.
- **Clear Display:** The remaining time is displayed in a large, easy-to-read `HH:MM:SS` format.
- **Audio & Visual Alerts:**
    - Plays an alarm sound (`alarm.mp3`) when the countdown reaches zero.
    - Shows a pop-up message box to notify you that the time is up.
    - Uses threading for audio playback to ensure the UI remains fully responsive.

<br>

## 🛠️ Technologies Used
- **Programming Language:** `Python`
- **GUI Library:** `PyQt5`
- **Audio Playback:** `Pygame`

<br>

## 🚀 Getting Started

Follow these instructions to get the application running on your system.

### Prerequisites
Ensure you have Python installed. You will also need to install the `PyQt5` and `Pygame` libraries. You can install them using pip:
```bash
pip install PyQt5 pygame
```

### Installation & Running
Clone the project from GitHub to your local machine:
```bash
git clone https://github.com/ErfanKhastar/Count-Down-Timer-With-PyQt5.git
cd Count-Down-Timer-With-PyQt5
```

### How To Run
Open your terminal or command prompt in that directory.  
Run the application with the following command:
```bash
python main.py
```








