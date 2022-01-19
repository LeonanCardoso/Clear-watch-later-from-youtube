import pyautogui
import time
# By - Leonan Cardoso
# Pause
pyautogui.PAUSE = 0.5

# Open browser
def openBrowser():
    pyautogui.press('winleft')
    pyautogui.write('opera')
    pyautogui.press('enter')

openBrowser()

# Write in Browser
def writeBrowser():
    time.sleep(1)
    pyautogui.write('https://www.youtube.com')
    pyautogui.hotkey('enter')
    time.sleep(4)

writeBrowser()

# Move cursor to watch later
def moveToWatchLater():
    pyautogui.moveTo(146, 453, duration=0.5)
    pyautogui.click(146, 453)
    time.sleep(2)

moveToWatchLater()

# Move cursor to more options for first video
def RemoveVideo():
    pyautogui.moveTo(1860, 321, duration=0.1)
    pyautogui.click(1860, 321)
    # Move cursor to delete video
    pyautogui.moveTo(1743, 454, duration=0.1)
    pyautogui.click(1743, 454)

# Repeater | Select the amount of videos to delete
for i in range(2):
    RemoveVideo()
