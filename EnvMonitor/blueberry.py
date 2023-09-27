import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import board
import time
import datetime
import csv

#Humidity
dht_pin = 4
dht_sensor = dht.DHT22
increment = 1

while True:
    hum, temp = dht.read_retry(dht_sensor, dht_pin)
    try:
        temp_f = round((temp * 9/5) + 32, 2)
        temp = round(temp,2)
        humidity = round(hum, 2)
    except:
        temp_f = None
        humidity = None
    data = [temp_f, humidity, datetime.datetime.now()]
    print("Temp: " + str(temp_f)+ '(' + str(temp) + ' C)' + " Humidity: " + str(humidity) + " " + str(datetime.datetime.now()))
    if increment < 10 and temp_f is not None:
        increment = increment + 1
        time.sleep(60)
    elif temp_f is not None:
        increment = 1
        with open('env-monitor/log/log.csv', 'a+') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        time.sleep(60)
    else:
        pass
GPIO.cleanup()
