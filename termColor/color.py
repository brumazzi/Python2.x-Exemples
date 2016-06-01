#!/usr/bin/env python

NONE=		"\033[0m"
BOLD=		"\033[1m"
HALFBRIGHT=	"\033[2m"
UNDERSCORE=	"\033[4m"
BLINK=		"\033[5m"
REVERSE=	"\033[7m"

#/****************************COLORS***************************************/
C_BLACK=	"\033[30m"
C_RED=		"\033[31m"
C_GREEN=	"\033[32m"
C_YELLOW=	"\033[33m"
C_BLUE=		"\033[34m"
C_MAGENTA=	"\033[35m"
C_CYAN=		"\033[36m"
C_GRAY=		"\033[37m"

#/**************************BACKGROUNDS************************************/
BG_BLACK=	"\033[40m"
BG_RED=		"\033[41m"
BG_GREEN=	"\033[42m"
BG_YELLOW=	"\033[43m"
BG_BLUE=	"\033[44m"
BG_MAGENTA=	"\033[45m"
BG_CYAN=	"\033[46m"
BG_GRAY=	"\033[47m"

from ctypes import cdll
from ctypes import *

lib = cdll.LoadLibrary("./color.so")

effect = lib.textEffect
clear = lib.clearEffect

#cyan = lib.CYAN

effect(C_MAGENTA)

print "Exibindo o texto!"

clear()
