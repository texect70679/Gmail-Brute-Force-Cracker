#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import platform
from os import  system

if platform.system() == 'Windows':
    SYS_PAUSE = 'pause'
    SYS_CLEAN = 'cls'
elif platform.system() == 'Linux':
    SYS_PAUSE = 'read -p "Press enter to continue" a'
    SYS_CLEAN = 'clear'
def SysCleanScreen():
    system(SYS_CLEAN)
def SysPause():
    system(SYS_PAUSE)
