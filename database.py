#!/usr/bin/env python3
# -*- coding: utf-8 -*-


INPUT = 0
OUTPUT = 1

PRIMARY = 0
FOREIGN = 1

data_types = [
    "int",
    "decimal",
    "varchar",
    "date",
    "time",
    "datetime"
]


class ModelException(Exception): pass

class Database:
    def __init__(self,name,tables,procedures):
        self.name = name
        self.tables = tables
        self.procedures = procedures
    def __str__(self):
        output = ""
        for t in self.tables:
            output += "{0}: {1}".format(t.name,", ".join([c.name for c in t.columns]))
        return output

class Table:
    def __init__(self,name,columns=[]):
        self.name = name
        self.columns = columns

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

class Key:
    def __init__(self,name,key_type,references=None):
        self.name = name
        self.key_type = key_type
        self.references = references
        if (self.key_type == FOREIGN) and (self.references==None):
            raise ModelException("Foreign key has to reference something.")

print(Database("test",[Table("tabulka",Column("sloupec","int",None))],[]))