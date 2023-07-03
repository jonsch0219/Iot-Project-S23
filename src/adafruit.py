import machine
import credentials
import ubinascii              # Conversions between binary data and various encodings
import time
import temperature
from mqtt import MQTTClient 
import led

NOTIFICATION_INTERVAL = 1800 #seconds
last_notification_sent_ticks = 0 #seconds
TEMPERATURES_INTERVAL = 20000    # milliseconds
last_temperature_sent_ticks = 0  # milliseconds

prev_led_status = None 
templimit = 100 #Hardcoded start value

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = credentials.ADAFRUIT_IO_USERNAME
AIO_KEY = credentials.ADAFRUIT_IO_KEY
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_TEMPERATURE_FEED = credentials.ADAFRUIT_TEMPERATURE
AIO_LED_FEED = credentials.ADAFRUIT_LED
AIO_TEMPLIMIT_FEED = credentials.ADAFRUIT_TEMPLIMIT
AIO_NOTIFICATION_FEED = credentials.ADAFRUIT_NOTIFICATION

def mqttConnectTo():
    # Use the MQTT protocol to connect to Adafruit IO
    client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

    client.set_callback(tempSlider)
    client.connect()
    client.publish(topic=AIO_TEMPLIMIT_FEED, msg=str(templimit)) #synchronizes the slider and templimit at start
    client.subscribe(AIO_TEMPLIMIT_FEED)
    print("Connected to %s, subscribed to %s topic" % (AIO_SERVER, AIO_TEMPLIMIT_FEED))
    return client

def tempSlider(topic, msg):
    global templimit
    print((topic, msg))
    templimit = int(msg)
    print("Max temperature set to", templimit) 

def sendLED(client, temp):
    global prev_led_status

    led_status = led.checkMaxTemp(temp)

    if led_status == prev_led_status:
        pass; #no change in data no need to send
    else:
        print("Publishing: {0} to {1} ... ".format(led_status, AIO_LED_FEED), end='')
        try:
            client.publish(topic=AIO_LED_FEED, msg=led_status)
            print("DONE")
        except Exception as e:
            print("FAILED")
        finally:
            prev_led_status = led_status
            
    if led_status == "ON":
        sendNotification(client)
    

def sendTemperature(client, filter_size):
    global last_temperature_sent_ticks
    
    if ((time.ticks_ms() - last_temperature_sent_ticks) < TEMPERATURES_INTERVAL):
        return; # Too soon since last one sent.

    
    temp = temperature.getTemperature(filter_size)
        
    print("Publishing: {0} to {1} ... ".format(temp, AIO_TEMPERATURE_FEED), end='')
    try:
        client.publish(topic=AIO_TEMPERATURE_FEED, msg=str(temp))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_temperature_sent_ticks = time.ticks_ms()
        sendLED(client, temp)

def sendNotification(client):
    global last_notification_sent_ticks

    if ((time.ticks_ms()/1000 - last_notification_sent_ticks) < NOTIFICATION_INTERVAL and last_notification_sent_ticks != 0):
        return;

    signal = "SEND"

    print("Publishing: {0} to {1} ... ".format(signal, AIO_NOTIFICATION_FEED), end='')
    try:
        client.publish(topic=AIO_NOTIFICATION_FEED, msg=signal)
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_notification_sent_ticks = time.ticks_ms()/1000
