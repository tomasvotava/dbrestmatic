#!/usr/bin/env python3
# -*- coding: utf-8 -*-


INPUT = 0
OUTPUT = 1


data_types = [
    "int",
    "decimal",
    "varchar",
    "date",
    "time",
    "datetime"
]

class Database:
    def __init__(self,name):
        self.name = name
        self.tables = []
        self.procedures = []

class Table:
    def __init__(self,name):
        self.name = name
        self.columns = []

class Procedure:
    def __init__(self,name):
        self.name = name
        self.parameters = []

class Column:
    def __init__(self,name,data_type,key):
        self.name = name
        self.type = data_type
        self.key = key

class Parameter:
    def __init__(self,name,direction):
        self.name = name
        self.direction = direction
