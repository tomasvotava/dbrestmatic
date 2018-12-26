#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


LEVEL_INFO = 0
LEVEL_WARNING = 1
LEVEL_ERROR = 2

LOG_LEVEL = LEVEL_ERROR

USE_STDOUT = True

def log_init(use_stdout=True):
    global USE_STDOUT
    sys.stdout = open("stdout.log","w")
    USE_STDOUT = use_stdout

def log(o,level=LEVEL_INFO):
    global LOG_LEVEL
    if level >= LOG_LEVEL:
        print(o)
        sys.stdout.flush()
        if USE_STDOUT:
            sys.__stdout__.write(str(o))
            sys.__stdout__.write("\n")

def set_log_level(level=LEVEL_ERROR):
    global LOG_LEVEL
    LOG_LEVEL = level

def WARN(o):
    log(o,LEVEL_WARNING)

def ERROR(o):
    log(o,LEVEL_ERROR)

def INFO(o):
    log(o,LEVEL_INFO)