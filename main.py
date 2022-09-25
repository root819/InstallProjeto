import os
import time


os.system('cls||clear')
time.sleep(1)

def banner():
    print('''\033[33m
        .---.        .-----------
       /     \  __  /    ------
      / /     \(  )/    -----
     //////   ' \/ `   ---
    //// / // :    : ---
   // /   /  /`    '--
  //          //..\\
         ====UU====UU====
             '//||\\`
               ''`` 
Siga-me no instagram: Daniel_edits9 
Espero ter te ajudado com essa script\033[m''')
banner()
print('\n')
menu = 0
while menu != 7:
    menu = int(input(('''
    [ 1 ] Metasploit-Framework
    [ 2 ] Nmap
    [ 3 ] Sqlmap 
    [ 4 ] Zphisher 
    [ 5 ] Distros Linux, Ubuntu etc.
    [ 6 ] Hasher
    [ 7 ] Sair 
    
    Coloque a opção desejada: ''')))
    if menu == 1:
     os.system('cls||clear')
     os.system('pkg update && pkg upgrade -y && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh')
     print('\n')
     print('Digite o seguinte codigo: chmod +x Metasploit.sh')
     print('Depois: ./metasploit.sh')
     print('Faça em ordem, Feche a script para dar esses comando :)')
    if menu == 2:
     os.system('cls||clear')
     os.system('apt update && apt upgrade && apt install nmap')
    if menu == 3:
     os.system('cls||clear')
     os.system('apt update && apt upgrade && pkg install python2 && pkg install git && git clone https://github.com/sqlmapproject/sqlmap')
     print('\n')
     print('Digite o comando a seguir: cd sqlmap')
     print('python2 sqlmap.py')
    if menu == 4:
     os.system('cls||clear')
     os.system('apt update && apt upgrade && apt install git php openssh curl -y && pkg install git && git clone https://github.com/htr-tech/zphisher')
     print('\n')
     print('Digite o comando a seguir: cd zphisher.sh')
     print('chmod +x zphisher.sh') 
     print('bash zphisher.sh')
    if menu == 5:
     os.system('cls||clear')
     os.system('apt update && apt upgrade && pkg install proot-distro')
     print('\n')
     print('Digites os comandos a seguir: proot-distro list [escolha a distro] ')
     print('proot-distro install *nome da distro*')
    if menu == 6:
     os.system('cls||clear')
     os.system('apt update && apt upgrade && pkg install python2 && pkg install git && git clone https://github.com/ciku370/hasher')
     print('\n')
     print('Digites os comandos a seguir: cd hasher ')
     print('python2 hash.py')
    elif menu == 7:
     print('Byee')
     time.sleep(2)
     os.system('cls||clear')
    
    
