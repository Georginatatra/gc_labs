#import requests
#url="https://maker.ifttt.com/trigger/Button_pressed/json/with/key/cgjs3v5bQ3BV6f1h7i9luA8OXpBuZi72Z-iUS3ITVOz"
#r= requests.get(url)
#print(r.status_code)

from gpiozero import Button, Buzzer
from signal import pause
import requests
from time import sleep

button_pressed=Button(18)

buzz = Buzzer(17)

def send_notify():
    url="https://maker.ifttt.com/trigger/Button_pressed/json/with/key/cgjs3v5bQ3BV6f1h7i9luA8OXpBuZi72Z-iUS3ITVOz"
    r= requests.get(url)
    buzz.on()
    sleep(2)
    print(r.status_code)
    buzz.off()


button_pressed.when_pressed = send_notify
pause()
