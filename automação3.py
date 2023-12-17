import pyautogui 

#SELECIONA A JANELA DESEJADA.
pyautogui.keyDown("alt")
pyautogui.keyDown("tab")
pyautogui.keyUp("tab")
pyautogui.keyUp("alt")

#NAVELA ATE A PRIMEIRA PASTA E DA UM CLICK.
pyautogui.moveTo(90, 350)
pyautogui.click(90, 350)

#NAVEGA ATE A PRIMEIRA CAIXA DE SELEÇÃO E DA UM CLICK.
pyautogui.moveTo(560, 225, duration=float(1))
pyautogui.click(560, 225, button="right", interval=float(1))

#NAVEGA ATE A SEGUNDA CAIXA DE SELEÇÃO E DA UM CLICK.
pyautogui.moveTo(310, 225)
pyautogui.click(310, 225, button="right", interval=float(1))

#NAVEGA ATE O BOTÃO ESVAZIAR E DA UM CLICK.
pyautogui.moveTo(290, 190,)
pyautogui.click(290, 190, button="right", interval=float(1))

pyautogui.moveTo(700, 450)
pyautogui.click(700, 450, button="right", interval=float(1))

