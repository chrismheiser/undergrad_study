#-------------------------------------------------------------------------------
# Name:        MySQL reader/writer
# Purpose:
#
# Author:      Jakub 'Yim' Dvorak
#
# Created:     26.10.2013
# Copyright:   (c) Jakub Dvorak 2013
# Licence:
#   ----------------------------------------------------------------------------
#   "THE BEER-WARE LICENSE" (Revision 42):
#   Jakub Dvorak wrote this file. As long as you retain this notice you
#   can do whatever you want with this stuff. If we meet some day, and you think
#   this stuff is worth it, you can buy me a beer in return.
#   ----------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import MySQLdb

from time import strftime,localtime
import datetime
from unidecode import unidecode

def connect():
    # Mysql connection setup. Insert your values here
    return MySQLdb.connect(host="tund", user="cmh553", passwd="122993Heelflip", db="cmh553")

def insertReading(tagId):
    db = connect()
    cur = db.cursor()
    currentTime=strftime("%Y%m%d%H%M%S", localtime())
    cur.execute("""INSERT INTO readings (tagId, time) VALUES (%s, %s)""",(tagId,currentTime))
    db.commit()
    db.close()
    if(row==None):
        return "None row"
    else:
        return unidecode(row[1]+", "+row[0])

