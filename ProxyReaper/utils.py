from colorama import Fore

red = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE

def error(msg):
    print(red + '[' + yellow + '!' + red + '] - ' + white + msg)

def alert(msg):
    print(red + '[' + blue + '#' + red + '] - ' + white + msg)

def action(msg):
    print(red + '[' + green + '+' + red + '] - ' + white + msg)

def get(txt):
    return input(red + '[' + blue + '#' + red +'] - ' + white + txt)

def save_to_file(file_dir, proxy):
    with open(file_dir, 'a') as f:
        f.write(proxy + '\n')