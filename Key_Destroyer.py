import keyboard
import pyautogui
import pyfiglet
import terminal_banner



#Baneer
a=pyfiglet.figlet_format("Key Destroyer")
b=terminal_banner.Banner(a)
print(b)

def Loope():
    while(True):

        ke = keyboard.is_pressed('a')

        if ke:
            be = pyautogui.typewrite('@')
            continue
        if keyboard.is_pressed('b'):
            pyautogui.typewrite('!')
            continue
        if keyboard.is_pressed('c'):
            pyautogui.typewrite('#')
            continue
        if keyboard.is_pressed('d'):
            pyautogui.typewrite('$')
            continue
        if keyboard.is_pressed('e'):
            pyautogui.typewrite('}')
            continue
        if keyboard.is_pressed('f'):
            pyautogui.typewrite('%')
            continue

        if keyboard.is_pressed('g'):
            pyautogui.typewrite('^')
            continue
        if keyboard.is_pressed('h'):
            pyautogui.typewrite('{')
            continue
        if keyboard.is_pressed('i'):
            pyautogui.typewrite('()')
            continue
        if keyboard.is_pressed('j'):
            pyautogui.typewrite('_')
            continue
        if keyboard.is_pressed('k'):
            pyautogui.typewrite('+')
            continue
        if keyboard.is_pressed('l'):
            pyautogui.typewrite('"')
            continue
        if keyboard.is_pressed('m'):
            pyautogui.typewrite('~')
            continue
        if keyboard.is_pressed('n'):
            pyautogui.typewrite('`')
            continue

        if keyboard.is_pressed('o'):
            pyautogui.typewrite('/')
            continue
        if keyboard.is_pressed('p'):
            pyautogui.typewrite(';')
            continue
        if keyboard.is_pressed('q'):
            pyautogui.typewrite('(')
            continue
        if keyboard.is_pressed('r'):
            pyautogui.typewrite('-')
            continue
        if keyboard.is_pressed('s'):
            pyautogui.typewrite('|')
            continue
            
        if keyboard.is_pressed('t'):
            pyautogui.typewrite('>')
            continue
        if keyboard.is_pressed('u'):
            pyautogui.typewrite('??')
            continue

        if keyboard.is_pressed('v'):
            pyautogui.typewrite('.')
            continue
        if keyboard.is_pressed('w'):
            pyautogui.typewrite('+')
            continue
        if keyboard.is_pressed('x'):
            pyautogui.typewrite('{(')
            continue
        if keyboard.is_pressed('y'):
            pyautogui.typewrite('-;')
            continue
        if keyboard.is_pressed('z'):
            pyautogui.typewrite(':')
            continue
            
            




















            
        

Loope()












   
   
