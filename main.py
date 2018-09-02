#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from lib.CGmail import  CGmail
from lib.showthing import InFo
from lib.printer import *
from lib.command import *


file_path = ' '
mail = ' '
count = 2

def GetArgc():
    global file_path
    global mail
    if len(sys.argv) == 1:
        printRed('\nCommand line useage:' + sys.argv[
            0] + ' ' + '[-u/--user] <User name> [-w/--wordlist] <Path of wordlist file>\n')
        file_path = raw_input("\nInput password list path(Path don\'t include: \") \n>")
        file_path.strip('"')
        mail = raw_input('\nEmail \n>')
    else:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] in ['-h', '--help']:
                printRed('\nCommand line useage:' + sys.argv[
                    0] + ' ' + '[-u/--user] <User name> [-w/--wordlist] <Path of wordlist file>\n')
                return 0
                break
            elif sys.argv[i] in ['-u', '--user']:
                i = i + 1
                mail = sys.argv[i]
            elif sys.argv[i] in ['-w', '--wordlist']:
                i = i + 1
                file_path = sys.argv[i]
            else:
                # print('Unknow parameter: '+ sys.argv[i] +' please use:'+ sys.argv[0]+' -h')
                # return 0
                # break
                continue

if __name__ == "__main__":
    InFo()
    if GetArgc() == 0:
        exit()
    else:
        CGmail(mail,file_path)
    print('\n')
    SysPause()
