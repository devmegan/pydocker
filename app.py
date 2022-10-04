class colours:
    INFO = '\033[96m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

print('python app running in docker container')

user_input = input('do you like it? [y/n]: ')

while True: 
    if user_input == 'y':
        print(colours.SUCCESS + 'yay :)' + colours.ENDC)
        exit()
    elif user_input == 'n': 
        print(colours.WARNING + 'sorry do hear it :(' + colours.ENDC)
        exit()
    else: 
        print(colours.ERROR + 'only use "y" or "n"' + colours.ENDC)
        user_input = input('do you like it? [y/n] ')