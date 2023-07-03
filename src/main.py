import adafruit
import connect

filter_size = 25 #How many temperatures the program computes the average temp on, must be more than 0

if filter_size  < 1:
    print ("Invalid filtering size!")
else:    
    try:
        ip = connect.connectToNetwork()
    except KeyboardInterrupt:
            print("Keyboard interrupt")
        
    client = adafruit.mqttConnectTo()

    try:                      
        while 1:
            client.check_msg()              
            adafruit.sendTemperature(client, filter_size)
    finally:                  
        client.disconnect()   
        client = None
        print("Disconnected from Adafruit IO.")