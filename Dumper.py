import discord
from discord import Webhook, RequestsWebhookAdapter
import os, sys, time, ctypes
import urllib.request
from pystyle import Center, Anime, Colors, Colorate, System
from colorama import Fore, Back, Style
from requests import get
import random
import webbrowser 


### COLORI E VAR ###
VERSIONETOOL = "0.1"
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
m = Fore.LIGHTMAGENTA_EX
r = Fore.LIGHTRED_EX

### SCHERMATA ###
def impostatitolo(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | github.com/itsmat")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} | github.com/itsmat\x07")
    else:
        pass

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def titolohome():
    print(f"""\n\n{m}
                ▓█████  ███▄ ▄███▓ ▒█████   ▄▄▄██▀▀▀██▓   ▓█████▄  █    ██  ███▄ ▄███▓ ██▓███  ▓█████  ██▀███  
                ▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒   ▒██  ▓██▒   ▒██▀ ██▌ ██  ▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
                ▒███   ▓██    ▓██░▒██░  ██▒   ░██  ▒██▒   ░██   █▌▓██  ▒██░▓██    ▓██░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
                ▒▓█  ▄ ▒██    ▒██ ▒██   ██░▓██▄██▓ ░██░   ░▓█▄   ▌▓▓█  ░██░▒██    ▒██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
                ░▒████▒▒██▒   ░██▒░ ████▓▒░ ▓███▒  ░██░   ░▒████▓ ▒▒█████▓ ▒██▒   ░██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
                ░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░  ▒▓▒▒░  ░▓      ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
                 ░ ░  ░░  ░      ░  ░ ▒ ▒░  ▒ ░▒░   ▒ ░    ░ ▒  ▒ ░░▒░ ░ ░ ░  ░      ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
                   ░   ░      ░   ░ ░ ░ ▒   ░ ░ ░   ▒ ░    ░ ░  ░  ░░░ ░ ░ ░      ░   ░░          ░     ░░   ░ 
                   ░  ░       ░       ░ ░   ░   ░   ░        ░       ░            ░               ░  ░   ░     
                                               ░                                                   
\n{w}""")#.replace('█', f'{y}█{b}'))

banner = r"""
░█████╗░░█████╗░██████╗░██╗░█████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗
██║░░╚═╝███████║██████╔╝██║██║░░╚═╝███████║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║
██║░░██╗██╔══██║██╔══██╗██║██║░░██╗██╔══██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║
╚█████╔╝██║░░██║██║░░██║██║╚█████╔╝██║░░██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░
"""[1:]

def transizione():
    clear()
    caricamento()
    clear()

def caricamento():
	carattere = ['|', '/', '-', '\\']
	for i in carattere+carattere+carattere:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Caricamento... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

global idserver
idserver = 'Nessun server impostato'
global token 
token = 'Nessun token impostato'
global tipodump
tipodump = 0
if not os.path.exists('Dumps'):
    os.makedirs('Dumps')

client = discord.Client()
encoding = sys.stdout.encoding

def main():
    global tipodump
    global idserver
    global token
    impostatitolo(f"Mat Emoji Dumper {VERSIONETOOL} - Caricamento")
    Anime.Fade(Center.Center(banner), Colors.green_to_red, Colorate.Vertical, time=1)
    #System.Size(160, 40)
    clear()
    impostatitolo(f"Mat Emoji Dumper {VERSIONETOOL}")
    titolohome()
    print(f"""      {y}[{b}+{y}]{g} Main:                                                                            {y}[{b}+{y}]{c} Settings:
          {y}[{w}1{y}]{g} Emoji dumper di un server                                                        {y}[{w}10{y}]{c} Imposta id server
          {y}[{w}2{y}]{g} Emoji dumper di tutti i server                                                   {y}[{w}11{y}]{c} Imposta client token  
          {y}[{w}3{y}]{g} Server Nuker                                                                    

                                                                                     {m}Made by Mat#3616 | github.com/itsmat
                                                                                     {m}ID Server     : {b}{idserver}
                                                                                     {m}Token         : {b}{token}
\t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global scelta
    scelta = input(f"""{y}[{b}#{y}]{w} : """)
    if scelta == '1' or scelta == '01':
        if token != 'Nessun token impostato':
            if idserver != 'Nessun server impostato':
                try:
                    tipodump = 1
                    print('Il dump partirà appena invierai/riceverai un messaggio')
                    client.run(token)
                except Exception as errore:
                    input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Errore [{errore}]!")
                    main()
            else:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} ID Server mancante [tasto 10 nella home]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Token mancante [tasto 11 nella home]!")
            main()
    if scelta == '2' or scelta == '02':
        if token != 'Nessun token impostato':
            try:
                tipodump = 2
                print('Il dump partirà appena invierai/riceverai un messaggio')
                client.run(token)
            except Exception as errore:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Errore [{errore}]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Token mancante [tasto 11 nella home]!")
            main()
    if scelta == '3' or scelta == '03':
        webbrowser.open_new_tab("https://github.com/itsmat/DiscordNukerTool")
        main()
    elif scelta == '10' or scelta == '010':
        transizione()
        dioporco = input(f'''{y}[{b}#{y}]{w} Inserisci l'id del server:    ''')
        idserver = dioporco
        main()
    elif scelta == '11' or scelta == '011':
        transizione()
        diocane = input(f'''{y}[{b}#{y}]{w} Inserisci il client-token:    ''')
        token = diocane
        main()
    elif scelta == 'dsc' or scelta == 'discord':
        webbrowser.open_new_tab("https://discord.gg/CzynytAxfh")
        main()
    elif scelta == 'exit' or scelta == 'chiudi':
        transizione()
        sys.exit()
    else:
        clear()
        main()



@client.event
async def on_message(message):
    global tipodump
    global idserver
    dump = 0
    if tipodump == 0:
        pass
    if tipodump == 1:
        emojipng = 0
        emojigif = 0
        server = await client.fetch_guild(idserver)
        numeroemoji = len(server.emojis)
        print(F'{y}Server: {server.name} [{server.id}] - {b}{numeroemoji}{w}')
        code = random.randint(0,9999)
        cartella = 'Dumps\\' + f'c{code}' + '\\' + server.name.translate({ord(c): None for c in '/<:"\\|?+*:>'})
        if numeroemoji > 0:
            if not os.path.exists(cartella):
                os.makedirs(cartella)
        print(f'{b}Scaricando le emoji...')
        try:
            if dump == 0:
                for emoji in server.emojis:
                    if emoji.animated:
                        nomeemoji = cartella + '\\' + emoji.name + '.gif'
                        emojigif += 1
                    else:
                        nomeemoji = cartella + '\\' + emoji.name + '.png'
                        emojipng += 1
                    if not os.path.exists(nomeemoji):
                        with open (nomeemoji, 'wb') as file:
                            request = urllib.request.Request(emoji.url, headers={'User-Agent': 'Mozilla/5.0'})
                            finale = urllib.request.urlopen(request).read()
                            file.write(finale) 
                dump = 1
                input(f'''{g}DUMP COMPLETATO CON SUCCESSO.

{r}Server: {server.name}
Emoji Scaricate: {emojipng}
Emoji Animate Scaricate: {emojigif}
Path: {cartella}{w}''')
                main()
            else:
                input('Errore')
                main()
        except:
            input('Errore')
            main()
    if tipodump == 2:
        servers = 0
        emojipng = 0
        emojigif = 0
        code = random.randint(0,9999)
        try:
            for server in client.guilds:
                servers += 1
                numeroemoji = len(server.emojis)
                print(F'{y}Server: {server.name} [{server.id}] - {b}{numeroemoji}{w}')
                cartella = 'Dumps\\' + f'c{code}' + '\\' + server.name.translate({ord(c): None for c in '/<:"\\|?+*:>'})
                if numeroemoji > 0:
                    if not os.path.exists(cartella):
                        os.makedirs(cartella)
                print(f'{b}Scaricando le emoji...')
                try:
                    for emoji in server.emojis:
                        if emoji.animated:
                            nomeemoji = cartella + '\\' + emoji.name + '.gif'
                            emojigif += 1
                        else:
                            nomeemoji = cartella + '\\' + emoji.name + '.png'
                            emojipng += 1
                        if not os.path.exists(nomeemoji):
                            with open (nomeemoji, 'wb') as file:
                                request = urllib.request.Request(emoji.url, headers={'User-Agent': 'Mozilla/5.0'})
                                finale = urllib.request.urlopen(request).read()
                                file.write(finale)
                except:
                    input('Errore')
                    main()
            try:
                input(f'''{g}DUMP COMPLETATO CON SUCCESSO.

{r}Server: {servers}
Emoji Scaricate: {emojipng}
Emoji Animate Scaricate: {emojigif}
Path: {cartella}{w}''')
                main()
            except:
                input('Errore')
                main()
        except:
            input('Errore')
            main()

main()
