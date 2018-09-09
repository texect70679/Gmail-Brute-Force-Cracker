#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import ctypes,sys,platform

if platform.system() == 'Windows':
  STD_INPUT_HANDLE = -10
  STD_OUTPUT_HANDLE = -11
  STD_ERROR_HANDLE = -12
  # 字型顏色定義 text colors
  FOREGROUND_BLUE = 0x09  # blue.
  FOREGROUND_GREEN = 0x0a  # green.
  FOREGROUND_RED = 0x0c  # red.
  FOREGROUND_YELLOW = 0x0e  # yellow.

  # 背景顏色定義 background colors
  BACKGROUND_YELLOW = 0xe0  # yellow.

    # get handle
  std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


  def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


    # reset white
  def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


    # green
  def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()


    # red
  def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()


    # yellow
  def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()

else:
  end = '\033[0m'
  red = '\033[1;31;40m'
  green = '\033[1;32;40m'
  yellow = '\033[1;33;40m'
  def printGreen(mess):
    print(green + mess + end)

    # red
  def printRed(mess):
    print(red + mess + end)
    # yellow
  def printYellow(mess):
    print(yellow + mess + end)
