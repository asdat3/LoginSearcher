import re, time, datetime, json,os
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

    if main_config["output"]["active"]:
        if os.path.exists('output.txt'):
            print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.RED + f'output.txt already existing! ' + Fore.RED + "hit enter to overwrite it")
            wait_iawdaiwdiuifesicsvwe = input('')

    if main_config["uregex"]["use_dictonary"]:
        with open('words.txt','r') as wwf:
            word_dictonary_list = [line.rstrip('\n') for line in wwf]

    try:
        with open(main_config["input_file"],'r') as f:
            content_as_list = [line.rstrip('\n') for line in f]
    except:
        content_as_list = []
        print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.RED + f'input file: {str(main_config["input_file"])} not found!')
        time.sleep(3)

    print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.BLUE + f'[0/{str(len(content_as_list))}] 0%')
    for content_line_now in content_as_list:
        global_line_counter = global_line_counter + 1

        percentage_now = int(global_line_counter) / int(len(content_as_list)) * 100
        if main_config["logging+"]:
            print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.BLUE + f'[{str(global_line_counter)}/{str(len(content_as_list))}] {str(percentage_now)}%',end="\r")
        elif main_config["show_%"]:
            print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.BLUE + f'[{str(global_line_counter)}/{str(len(content_as_list))}] {str(percentage_now)}%',end="\r")

        time.sleep(main_config["artifical_delay"])

        for word_now in content_line_now.split():
            global_word_counter = global_word_counter + 1
            
            #search for keywords
            if main_config["keywordsearch"]:
                for keyword_now in main_config["keywordlist"]:
                    if keyword_now in word_now:
                        if main_config["logging+"]:
                            print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.WHITE + f'Keyword: {str(keyword_now)} found!')
                        if main_config["output"]["discord_format"]:
                            kw_global_interesting_lines.append(f'**{str(global_line_counter-1)}:** ' + str(content_as_list[int(global_line_counter - 2)]).replace(str(keyword_now),'*'+str(keyword_now)+'*'))
                            kw_global_interesting_lines.append(f'**{str(global_line_counter)}:** '   + str(content_as_list[global_line_counter - 1]).replace(str(keyword_now),'*'+str(keyword_now)+'*'))
                            kw_global_interesting_lines.append(f'**{str(global_line_counter+1)}:** ' + str(content_as_list[global_line_counter]).replace(str(keyword_now),'*'+str(keyword_now)+'*'))
                        else:
                            kw_global_interesting_lines.append(f'{str(global_line_counter-1)}: ' + str(content_as_list[int(global_line_counter - 2)]))
                            kw_global_interesting_lines.append(f'{str(global_line_counter)}: '   + str(content_as_list[global_line_counter - 1]))
                            kw_global_interesting_lines.append(f'{str(global_line_counter+1)}: ' + str(content_as_list[global_line_counter]))
                        kw_global_interesting_lines_raw.append(str(content_as_list[global_line_counter - 2]))
                        kw_global_interesting_lines_raw.append(str(content_as_list[global_line_counter - 1]))
                        kw_global_interesting_lines_raw.append(str(content_as_list[global_line_counter]))

            #get all that might be
            if main_config["uregex"]["active"]:
                if not len(word_now) < int(main_config["uregex"]["min_letters"]):
                    if not len(word_now) > int(main_config["uregex"]["max_letters"]):
                        if main_config["uregex"]["use_dictonary"]:
                            if not word_now in word_dictonary_list:
                                pw_var = re.search(r"^(?:(?:(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]))|(?:(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))|(?:(?=.*[0-9])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))|(?:(?=.*[0-9])(?=.*[a-z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))).{8,32}$",word_now)
                                if pw_var:
                                    if main_config["logging+"]:
                                        print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.WHITE + f'Possible pw: {str(pw_var.group())} found!')
                        else:
                            pw_var = re.search(r"^(?:(?:(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]))|(?:(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))|(?:(?=.*[0-9])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))|(?:(?=.*[0-9])(?=.*[a-z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))).{8,32}$",word_now)
                            if pw_var:
                                if main_config["logging+"]:
                                    print(Fore.WHITE + Style.BRIGHT + datetime.datetime.now().strftime("%H:%M:%S") + ourcolor + ' | ' + Fore.WHITE + f'Possible pw: {str(pw_var.group())} found!')

            #output
            if main_config["output"]["active"]:
                with open('output.txt','w') as outf:

                    #Keyword Result:
                    if main_config["output"]["discord_format"]:
                        outf.write('__**Keyword Result:**__\n')
                    else:
                        outf.write('Keyword Result:\n')

                    for kw_interesting_line_now in kw_global_interesting_lines:
                        outf.write(str(kw_interesting_line_now)+'\n')

banner()
main()