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
            pyautogui.press('backspace',interval=0.1)
            be = pyautogui.typewrite('@',interval=0.1)
            
            continue
        if keyboard.is_pressed('b'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('!',interval=0.1)
            continue
        if keyboard.is_pressed('c'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('#',interval=0.1)
            continue
        if keyboard.is_pressed('d'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('$',interval=0.1)
            continue
        if keyboard.is_pressed('e'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('}',interval=0.1)
            continue
        if keyboard.is_pressed('f'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('%',interval=0.1)
            continue

        if keyboard.is_pressed('g'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('^',interval=0.1)
            continue
        if keyboard.is_pressed('h'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('{',interval=0.1)
            continue
        if keyboard.is_pressed('i'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('()',interval=0.1)
            continue
        if keyboard.is_pressed('j'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('_',interval=0.1)
            continue
        if keyboard.is_pressed('k'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('+',interval=0.1)
            continue
        if keyboard.is_pressed('l'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('"',interval=0.1)
            continue
        if keyboard.is_pressed('m'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('~',interval=0.1)
            continue
        if keyboard.is_pressed('n'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('`',interval=0.1)
            continue

        if keyboard.is_pressed('o'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('/',interval=0.1)
            continue
        if keyboard.is_pressed('p'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite(';',interval=0.1)
            continue
        if keyboard.is_pressed('q'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('(',interval=0.1)
            continue
        if keyboard.is_pressed('r'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('-',interval=0.1)
            continue
        if keyboard.is_pressed('s'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('|',interval=0.1)
            continue
            
        if keyboard.is_pressed('t'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('>',interval=0.1)
            continue
        if keyboard.is_pressed('u'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('??',interval=0.1)
            continue

        if keyboard.is_pressed('v'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('.',interval=0.1)
            continue
        if keyboard.is_pressed('w'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('+',interval=0.1)
            continue
        if keyboard.is_pressed('x'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('{(',interval=0.1)
            continue
        if keyboard.is_pressed('y'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite('-;',interval=0.1)
            continue
        if keyboard.is_pressed('z'):
            pyautogui.press('backspace',interval=0.1)
            pyautogui.typewrite(':',interval=0.1)
            continue
            
            




















            
        

Loope()












   
   
