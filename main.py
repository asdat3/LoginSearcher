import re, time, datetime, json
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
        config_r = json.load(f)
    return(config_r)

def main():
    main_config = read_config()

    global_word_counter = 0
    global_line_counter = 0
    kw_global_interesting_lines = []
    kw_global_interesting_lines_raw = []


    if main_config["uregex"]["use_dictonary"]:
        with open('words.txt','r') as wwf:
            word_dictonary_list = [line.rstrip('\n') for line in wwf]

    try:
        with open(main_config["input_file"],'r') as f:
            content_as_list = [line.rstrip('\n') for line in f]
    except:
        content_as_list = []
        print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.RED + f'input file: {str(main_config["input_file"])} not found!')

    for content_line_now in content_as_list:
        global_line_counter = global_line_counter + 1
        for word_now in content_line_now.split():
            global_word_counter = global_word_counter + 1
            
            #search for keywords
            if main_config["keywordsearch"]:
                for keyword_now in main_config["keywordlist"]:
                    if keyword_now in word_now:
                        if main_config["logging+"]:
                            print("\n" + Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.WHITE + f'Keyword: {str(keyword_now)} found!')
                        kw_global_interesting_lines.append(f'{str(global_line_counter)-1}: ' + content_as_list[global_line_counter - 2])
                        kw_global_interesting_lines.append(f'{str(global_line_counter)}: '   + content_as_list[global_line_counter - 1])
                        kw_global_interesting_lines.append(f'{str(global_line_counter)+1}: ' + content_as_list[global_line_counter])
                        kw_global_interesting_lines_raw.append(content_as_list[global_line_counter - 2])
                        kw_global_interesting_lines_raw.append(content_as_list[global_line_counter - 1])
                        kw_global_interesting_lines_raw.append(content_as_list[global_line_counter])

            #get all that might be
            if main_config["uregex"]["active"]:
                if main_config["uregex"]["use_dictonary"]:
                    if not word_now in word_dictonary_list:
                        
                else:


banner()
main()