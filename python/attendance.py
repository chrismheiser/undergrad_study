import nfc
import mysql
import sys
import tty
import termios
import logging
import time

import RPi.GPIO as GPIO

#Enable debug logging into log
DEBUG=True
#Enable printing informations to std. output
VERBOSE=True

if(DEBUG):
    logging.basicConfig(format='%(asctime)s %(message)s',filename='attendance.log', level=logging.DEBUG)

def debug(message):
    logging.debug(message)

def read():
    cardId=nfc.readNfc()
    return cardId

def readNfc():
    cardId = read()
    name = mysql.insertReading(cardId)

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
def getOneKey():
    try:
        tty.setcbreak(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        return ord(ch)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def initGpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

def main():
    GPIO.cleanup()
    try:
        initGpio()
        while True:
            a = getOneKey()
            if 47 < a < 58:
                readNfc(a)
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
    GPIO.cleanup()

if __name__ == '__main__':
    debug("----------========== Starting session! ==========----------")
    main()
