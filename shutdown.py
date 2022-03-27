# author: ononemli

from pyfiglet import Figlet
from time import sleep
import os

tool = Figlet(font='digital')
print(tool.renderText('Shutdown  Restart  Tool'))

ononemli = Figlet(font='doom')
print(ononemli.renderText('ononemli'))

print('1 > Shutdown Computer' + '\n' + '2 > Restart Computer' + '\n' + '3 > Log of' + '\n' + '4 > Exit' + '\n' + '\n' 'What is your choice > ')
sleep(0.5)
command = int(input())

if command == 1:
    print('\n'+'Shutting Down')
    sleep(3)
    os.system("shutdown /s")

elif command == 2:
    print('\n'+'Restarting')
    sleep(3)
    os.system("shutdown /r")

elif command == 3:
    print('\n'+'Logging of')
    sleep(3)
    os.system("shutdown /l")

elif command == 4:
    exit()

else:
    print('\n' + 'Incorrect entry')
    input('\n' + 'Press enter to exit')
    if input: exit()