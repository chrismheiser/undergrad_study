import MySQLdb
from time import strftime,localtime
import datetime
from unidecode import unidecode

def connect():
    # Mysql connection setup. Insert your values here
<<<<<<< HEAD
    return MySQLdb.connect(host="tund.cefns.nau.edu", user="cmh553", passwd="122993Heelflip", db="cmh553")
=======
    return MySQLdb.connect(host="tund", user="cmh553", password="122993Heelflip", db="cmh553")
>>>>>>> 6b9883fe434a9141f3715d1d7a57c3a388dd0de6

def insertReading(tagId):
    db = connect()
    cur = db.cursor()
    currentTime=strftime("%Y%m%d%H%M%S", localtime())
    cur.execute("""INSERT INTO readings (tagId, time) VALUES (%s, %s, %s)""",(tagId,currentTime))
    db.commit()
    db.close()
