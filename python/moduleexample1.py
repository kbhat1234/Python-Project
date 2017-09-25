import os
from os import name, path
import datetime
from datetime import date, time, timedelta
import time

def moduleName():
           "printing name of the OS using os.name"
           print "Name of the OS: ", os.name

def modulePath():
           "prints whether item exists, item is a file, and item is a directory"
           print "Item exists: ", path.exists("C:\\Python27\\Dog.py")
           print "Item is a file: ", path.isfile("C:\\Python27\\Dog.py")
           print "Item is a directory: ", path.isdir("C:\\Python27\\")

def modulePathAndSplitPath():
           "prints path info and split the path name and file name"
           print "Path of file: ", path.realpath("Dog.py")
           print "Path and filename as split: ", path.split(path.realpath("Dog.py"))

def moduleLastModifiedFile():
           t = time.ctime(path.getmtime("C:\\Python27\\Dog.py"))
           print "File last modified: (format 1) ", t
           print "File last modified: (format 2) ", datetime.datetime.fromtimestamp(path.getmtime("C:\\Python27\\Dog.py"))
