import re, time, datetime
from colorama import Fore, Style, init

init()
ourcolor = Fore.CYAN

def banner():
    print("" + Style.BRIGHT + ourcolor)
    print("""     _                 _       _____                     _     
    | |               (_)     /  ___|                   | |    
    | |     ___   __ _ _ _ __ \ `--.  ___  __ _ _ __ ___| |__  
    | |    / _ \ / _` | | '_ \ `--. \/ _ \/ _` | '__/ __| '_ \ 
    | |___| (_) | (_| | | | | /\__/ /  __/ (_| | | | (__| | | |
    \_____/\___/ \__, |_|_| |_\____/ \___|\__,_|_|  \___|_| |_|
                  __/ |                                        
                 |___/                                         """)
    print("\n" + Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.WHITE + 'coded by KyuDev')

def read_config():
    with open('config.json','r') as f:
        config_r = json.read(f)
    return(config_r)

def main():
    main_config = read_config()

    with open('words.txt','r') as wwf:
        word_dictonary_list = [line.rstrip('\n') for line in wwf]

    with open(main_config["input_file"],'r') as f:
        content_as_list = [line.rstrip('\n') for line in f]
    for content_line_now in content_as_list:

