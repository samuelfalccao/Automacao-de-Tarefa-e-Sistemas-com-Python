# 1 Passo: pip install pyautogui > pyperclip > python-time

import pyautogui as pa 
import pyperclip as pp
import time

# Abrir o Google Chrome, Entrar no Whatsapp Web e Enviar as NF'S 

time.sleep(3)

pa.PAUSE=4

# Acessar Google Chrome
pa.hotkey("win","s")
pa.write("Google Chrome")
pa.press("enter")

# Acessar Whatsapp no Navegador
time.sleep(4)
pa.hotkey("win", "up")
time.sleep(2)
pa.hotkey("ctrl","t")
time.sleep(2)
pa.write("https://web.whatsapp.com/")
pa.press("enter")

# Clicar na Barra de Pesquisa & Escrever o nome do Grupo 
time.sleep(20)
#pa.click(x=174, y=182, clicks=1)
pa.hotkey("ctrl","alt","/")
pa.write("Notas")

# clicar enter -> grupo Notas
time.sleep(2)
pa.press("enter")

# clicar em Anexo:
time.sleep(2)
pa.click(x=506, y=829, clicks=1)

# clicar em Documento
time.sleep(2)
pa.click(x=510, y=559, clicks=1)

# Escrever Endereço da Pasta onde estão as NF'S e Clicar Enter
time.sleep(3)
endOne = (r"C:\Scanner")
pp.copy(endOne)
pa.hotkey("ctrl","v") # após o comando pp.copy acrescente o comando para colar
time.sleep(2)
pa.press("enter")

# Clique no Espaço em Branco da Pasta > Selecionar as NF'S > Enter
time.sleep(2)
pa.click(x=330, y=308, clicks=1)
time.sleep(2)
pa.hotkey("ctrl", "a")
time.sleep(2)
pa.press("enter")

# Clicar em Enter para Enviar
time.sleep(10)
pa.press("enter")

# Desconectar Whatsapp
time.sleep(100)
pa.click(x=373, y=103, clicks=1)
time.sleep(3)
pa.click(x=248, y=278, clicks=1)
time.sleep(3)
pa.click(x=801, y=456)

time.sleep(3)
name = "Samuel Falcão"
print("Hello, " + name + "a tarefa foi realizada com sucesso!")
