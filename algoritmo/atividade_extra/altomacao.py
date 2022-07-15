# programa para span
import pyautogui
pyautogui.PAUSE = 1
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('g')
# pyautogui.keyUp('ctrl')
# pyautogui.keyUp('g')


cont = 1
pyautogui.hotkey('alt', 'f2')
while cont < 15:
    pyautogui.typewrite ('teste ')
    pyautogui.press('enter')
    cont += 1
# pyautogui.typewrite('')
# pyautogui.press('enter')
# teste


