#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logger import log, LEVEL_WARNING, LEVEL_ERROR, LEVEL_INFO, log_init, set_log_level, WARN, ERROR, INFO

log_init(use_stdout=True)
set_log_level(LEVEL_INFO)


INFO("Importing required modules...")

import os
import json
import sys

try:
    import mysql.connector as dbc
except ImportError as e:
    ERROR("mysql.connector library must be installed.\nTry pip install mysql-connector")
    sys.exit(0)

import database

INFO("Loading configuration...")

if not os.path.exists("config.json"):
    ERROR("config.json not found. Please consult config-sample.json when creating one.")
    sys.exit(0)

conf = {}

with open("config.json") as conf_fid:
    conf = json.load(conf_fid)

try:
    connection = dbc.connect(user=conf["db"]["user"],host=conf["db"]["host"],port=conf["db"]["port"],passwd=conf["db"]["pass"],db=conf["db"]["db"])
except (dbc.errors.ProgrammingError, dbc.errors.InterfaceError) as e:
    ERROR("Error connecting to DB. Please check your config.json for errors.")
    ERROR(e)
    sys.exit(0)

