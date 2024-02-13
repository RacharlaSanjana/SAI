from pynput.keyboard import Key,Controller
import pyautogui
from time import sleep

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def cut():
    pyautogui.hotkey('ctrl', 'x')

def copy():
    pyautogui.hotkey('ctrl', 'c')

def paste():
    pyautogui.hotkey('ctrl', 'v')

def undo():
    pyautogui.hotkey('ctrl', 'z')

def redo():
    pyautogui.hotkey('ctrl', 'y')

def delete():
    pyautogui.press('del')

def select_all():
    pyautogui.hotkey('ctrl', 'a')

# Music Playback
def play_pause():
    pyautogui.press('space')

def next_track():
    pyautogui.hotkey('ctrl', 'right')

def previous_track():
    pyautogui.hotkey('ctrl', 'left')

def seek_forward():
    pyautogui.hotkey('shift', 'right')

def seek_backward():
    pyautogui.hotkey('shift', 'left')

def play_current():
    pyautogui.press('enter')

def toggle_shuffle_mode():
    pyautogui.hotkey('ctrl', 's')

def cycle_repeat_modes():
    pyautogui.hotkey('ctrl', 'r')

# Navigation
def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')

def open_search():
    pyautogui.hotkey('ctrl', 'l')

def show_search_in_playlist_box():
    pyautogui.hotkey('ctrl', 'f')

# Zoom
def zoom_in():
    pyautogui.hotkey('ctrl', 'plus')

def zoom_out():
    pyautogui.hotkey('ctrl', 'minus')

def reset_zoom():
    pyautogui.hotkey('ctrl', '0')
