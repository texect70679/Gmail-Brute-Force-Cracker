#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from lib.printer import *
from command import *

class InFo(object):
    def __init__(self):
        printGreen('=================================================\n')
        printGreen(u'             LBT Cracker                   \n')
        printGreen('=================================================\n')
        printGreen('Version:2.2                             By LBT   \n\n')

class ShowSucess(object):
    def __init__(self,ac,pw):
        self.ac = ac
        self.pw = pw
        printYellow('\n[-]Account:')
        printGreen(self.ac)
        printYellow('\n\n[-]Password:')
        printRed(self.pw)
        print('\n\nDon\'t forget to thank LBT ^_^')
        SysPause()