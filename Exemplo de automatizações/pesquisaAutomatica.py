#esse codigo usa o pyautogui ele foi feito para ser utilizado no linux
#e está configurado para a minha resolução de tela então se for utiliza-la tera que alterar o x e y 
# esse é um dos primeiros que eu irei postar sobre automatização de ações com python 

import pyautogui 
pyautogui.PAUSE = 2.5

pyautogui.hotkey('ctrl', 'alt', 't')
pyautogui.typewrite('firefox')
pyautogui.hotkey('enter')
pyautogui.hotkey('alt', 'tab')
pyautogui.typewrite('https://www.google.com/')
pyautogui.hotkey('enter')
pyautogui.typewrite('receita de almondegas')
pyautogui.hotkey('enter')
pyautogui.click(x=459, y=715)

