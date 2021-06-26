import schedule
import time
from gpiozero import LED

red = LED(22)
amber = LED(27)
green = LED(17)

def redOn():
    red.on()
    amber.off()
    green.off()

def greenOn():
    red.off()
    amber.off()
    green.on()

def amberOn():
    red.off()
    amber.on()
    green.off()

red.on()
schedule.every().day.at("06:30:00").do(amberOn)
schedule.every().day.at("07:00:00").do(greenOn)
schedule.every().day.at("19:00:00").do(amberOn)
schedule.every().day.at("19:30:00").do(redOn)

while True:
    schedule.run_pending()
    time.sleep(1)