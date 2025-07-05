from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel, QPushButton, QMessageBox
from PyQt5 import uic
import sys
from PyQt5.QtCore import QTimer
from threading import Thread
import time
import pygame
from Count_Down_Timer_2 import Ui_SecondWindow, QtWidgets


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi("Count_Down_Timer.ui", self)
        self.setWindowTitle("Count Down Timer")

        # Define Our Widgets
        self.hour_label = self.findChild(QLabel, "hour_label")
        self.minutes_label = self.findChild(QLabel, "minutes_label")
        self.seconds_label = self.findChild(QLabel, "seconds_label")
        self.status_label = self.findChild(QLabel, "status_label")
        self.timer_label = self.findChild(QLabel, "timer_label")
        self.hour_CB = self.findChild(QComboBox, "hour_comboBox")
        self.minutes_CB = self.findChild(QComboBox, "minutes_comboBox")
        self.seconds_CB = self.findChild(QComboBox, "seconds_comboBox")
        self.set_button = self.findChild(QPushButton, "set_pushButton")

        # Add Item To ComboBoxes
        self.hour_CB.addItems(str(f"{i:02}") for i in range(0, 24))
        self.minutes_CB.addItems(str(f"{i:02}") for i in range(0, 60))
        self.seconds_CB.addItems(str(f"{i:02}") for i in range(0, 60))

        # Click The Button
        self.set_button.clicked.connect(self.set)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_remaining_time)
        self.time_left = 0
        self.timer_running = True
        self.reset_time = 0
        pygame.mixer.init()

        # Show The App
        self.show()

    # Set The Timer
    def set(self):
        # Get Numbers From ComboBoxes
        hours = int(self.hour_CB.currentText())
        minutes = int(self.minutes_CB.currentText())
        seconds = int(self.seconds_CB.currentText())
        # Count Total Seconds
        self.time_left = (hours * 3600) + (minutes * 60) + seconds
        self.reset_time = self.time_left
        # Change The Status Label
        self.status_label.setText("Timer Started!")
        # Open Timer Window
        self.openWindow()

    # Update Remaining Time To Show On Screen
    def update_remaining_time(self):
        # First Check The Timer Is Running Or Not
        if self.timer_running:
            if self.time_left > 0:
                self.time_left -= 1
                # Count The Hours, Minutes, Seconds
                hours, remain = divmod(self.time_left, 3600)
                minutes, seconds = divmod(remain, 60)
                # Show Remaining Time
                time_text = f"{hours:02}:{minutes:02}:{seconds:02}"
                self.Ui.countdown_label.setText(time_text)
                # Reset The Label When The Timer Finish
            elif self.time_left == 0:
                self.status_label.setText("Ready To Set!")
                self.play_alarm()
                self.timer.stop()
        else:
            self.timer.stop()

    # Open The Timer Window
    def openWindow(self):
        # Open Window
        self.second_window = QtWidgets.QMainWindow()
        self.Ui = Ui_SecondWindow()
        self.Ui.setupUi(self.second_window)
        # Show The Timer On Label
        if self.time_left > 0:
            self.timer.start(1000)
            self.update_remaining_time()
        # Show The Window
        self.second_window.show()
        # Connect The Buttons In SecondWindow
        self.Ui.PR_pushButton.clicked.connect(self.pause_resume)
        self.Ui.reset_pushButton.clicked.connect(self.reset)

    def pause_resume(self):
        # Change The Timer Status
        self.timer_running = not self.timer_running
        # Check For Run The Timer Or Stop It
        if self.timer_running:
            self.timer.start(1000)
            self.update_remaining_time()
        else:
            self.timer.stop()

    # Reset The Timer
    def reset(self):
        self.time_left = self.reset_time
        # Count The Hours, Minutes, Seconds Again
        hours, remain = divmod(self.time_left, 3600)
        minutes, seconds = divmod(remain, 60)
        # Show The Time On Label
        self.Ui.countdown_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
        # Change Status Label
        self.status_label.setText("Timer Started!")
        # Run The Timer Again
        self.timer_running = True
        self.timer.start(1000)
        self.update_remaining_time()

    # Play Alarm
    def play_alarm(self):
        def alarm_thread():
            # Alarm Sound Location
            pygame.mixer.music.load("alarm.mp3")
            # Loop until manually stopped
            pygame.mixer.music.play(-1)
            # Stop The Sound After 5 Seconds
            time.sleep(5)
            pygame.mixer.music.stop()
        # Start The Thread
        Thread(target=alarm_thread, daemon=True).start()
        # Set The MessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Time\"s Up!")
        msg.setText("The countdown has finished!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        # Stop The Sound When MessageBox Has Closed
        msg.buttonClicked.connect(lambda: pygame.mixer.music.stop())
        # Run The MessageBox
        msg.exec_()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
