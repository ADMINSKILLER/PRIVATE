import time
import os
import colorama
import webbrowser
from subprocess import call
from sys import platform

vermelho = '\033[1;31m'
reset = '\033[m'

def clear():
    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    call(command, shell=True)
    
colorama.init()

clear()
nome = input('''

\033[1;33m──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
\033[1;31m
Digite seu nome:\033[m ''')
clear()
     
erro = vermelho + '''
 ____                 _       /            _
|  _ \ __ _ _ __ __ _| |__   ___ _ __  ___| |
| |_) / _` | '__/ _` | '_ \ / _ \ '_ \/ __| |
|  __/ (_| | | | (_| | |_) |  __/ | | \__ \_|
|_|   \__,_|_|  \__,_|_.__/ \___|_| |_|___(_)


Você FUDEU o script.

\033[m'''

logo = reset + '''
░░░░░░░░░░░░░░░░░░░░░▄▀░░▌
░░░░░░░░░░░░░░░░░░░▄▀▐░░░▌
░░░░░░░░░░░░░░░░▄▀▀▒▐▒░░░▌
░░░░░▄▀▀▄░░░▄▄▀▀▒▒▒▒▌▒▒░░▌
░░░░▐▒░░░▀▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░░░▌▒░░░░▒▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▐▒░░░░░▒▒▒▒▒▒▒▒▒▌▒▐▒▒▒▒▒▀▄
░░░░▌▀▄░░▒▒▒▒▒▒▒▒▐▒▒▒▌▒▌▒▄▄▒▒▐
░░░▌▌▒▒▀▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒█▄█▌▒▒▌
░▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▄▀█▌▒▒▒▒▒▀▀▒▒▐░░░▄
▀▒▒▒▒▌▒▒▒▒▒▒▒▄▒▐███▌▄▒▒▒▒▒▒▒▄▀▀▀▀
▒▒▒▒▒▐▒▒▒▒▒▄▀▒▒▒▀▀▀▒▒▒▒▄█▀░░▒▌▀▀▄▄
▒▒▒▒▒▒█▒▄▄▀▒▒▒▒▒▒▒▒▒▒▒░░▐▒▀▄▀▄░░░░▀
▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▄▒▒▒▒▄▀▒▒▒▌░░▀▄
▒▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▒▀▀▀▀▒▒▒▄▀
\033[m'''

logo1 = vermelho + '''｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡
'''
 
by = '\033[1;33mDeveloped by Causs\033[m'
 
clear()
print(logo)
print(logo1)
print(by)
menu =  input('''

Bem vindo \033[1;31m{}!\033[m Obrigado por utilizar o SKILLER Bot, Skiller agradece

\033[1;31m[\033[m1\033[1;31m]\033[m - Instalar Bot
\033[1;31m[\033[m2\033[1;31m]\033[m - Insta do Skiller
\033[1;31m[\033[m3\033[1;31m]\033[m - Canal do Skiller
\033[1;31m[\033[m0\033[1;31m]\033[m - Sair

\> \033[m '''.format(nome))
    
if menu == '0':
    print('\n\n\033[1;31mSaindo...\n\n')
    os.exit()
elif menu == '1':
    def spam():
        if platform not in ('win32', 'cygwin'):
            command = 'sh install.sh'
        call(command, shell=True)
    spam()
if menu == '67':
        if platform not in ('win32', 'cygwin'):
            command = 'bash install.sh'
            call(command, shell=True)
if menu == '2':
    if platform not in ('win32', 'cygwin'): 
       os.system("termux-open-url https://ch")       
if menu == '3':
    if platform not in ('win32', 'cygwin'): 
       os.system("termux-open-url https://youtube.com/c/SKILLERFFOFC")          
if menu == '18':
    if platform not in ('win32', 'cygwin'): 
       os.system("termux-open-url https://www.youtube.com/channel/UCpB3qh2Sp3K23s9a2Q-Gf-g?view_as=subscriber")
if menu == '20':
    if platform not in ('win32', 'cygwin'): 
       os.system("termux-open-url https://instagram.com/lostkkj_?igshid=192snsyd6kzxn") 
if menu == '4':
    if platform not in ('win32', 'cygwin'): 
       os.system("termux-open-url https://instagram.com/causs_dv?igshid=7zx0fzggirtv") 