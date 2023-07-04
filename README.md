# Iot-Project-S23
Name: Jonas Scharin

Student ID: js226yd

## Overview
This project monitors the temperature and uses a LED and a discord bot to notify when the temperature has exceeded a upperbound which is dynamically set by the user. For someone with a basic knowledge of programming, webhooks, git and breadboards following this tutorial and setting up the project should not take more than an hour.

## Objective
I have chosen to do create this device to in a fun and rewarding way learn about "Internet of Things. Why this specific project was chosen is because I want to be able to monitor and control the temperature in my home in a preemptive way, which in this case means that the user should have a greater awarness of the the temperature in a specific environment. The temperature upper bound which is dynamically set by the user serves as a threshold. When the threshold is exceeded the user will be informed by a lit up LED and a notification on discord. This feature helps the user have greater control over the environment.

Example: User does not want the temperature in its appartment to exceed 30 degrees so it sets the upper bound to 30 degrees. When the upper bound is passed the user will be informed and can take actions such as opening a window, turning on a fan e.t.c to keep the temperature below its upper bound.

## Material
The Rasberry Pi Pico W is the microcontroller used for this project. See datasheet [here](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf).

The MCP9700 TO-92 Temperature sensor has a range of -40° - 125°C, which works fine for this project as long as your not monitoring extreme environments. The sensor outputs linear voltage (analog).

I have chosen to use a 5mm red diffuse 1500mcd LED to turn on when the temperature has exceeded its upper bound. The choice of LED here is not strict at all.

To connect all the components I have used 30cm male/male jumper wires and a 840 tie-point breadboard. An alternative option here would be to buy male/female wires and connect them directly to the components, this would remove the need of a breadboard and give the device increased flexibility.

To connect to the Rasberry Pi Pico W to my computer I used a 1.8 meter A-male to MicroB USB cable.

| Hardware | Picture | Link |
| -------- | ------- | ---- |
| Rasberry Pi Pico W | <img src="img/PicoW.jpg" width="200"> | [Electrokit link](https://www.electrokit.com/en/product/raspberry-pi-pico-w/) |
| MCP9700 TO-92 Temperature sensor | <img src="img/tempsensor.jpg" width="200"> | [Electrokit link](https://www.electrokit.com/en/product/mcp9700-e-to-to-92-temperature-sensor/) |
| LED 5mm red diffuse 1500mcd | <img src="img/led.jpg" width="200"> | [Electrokit link](https://www.electrokit.com/en/product/led-5mm-rod-diffus-1500mcd/) |
| Solderless Breadboard 840 tie-points | <img src="img/breadboard.jpg" width="200"> | [Electrokit link](https://www.electrokit.com/en/product/solderless-breadboard-840-tie-points-2/) |
| Jumper wires 40-pin 30cm male/male | <img src="img/cables.jpg" width="200"> | [Electrokit link](https://www.electrokit.com/en/product/jumper-wires-40-pin-30cm-male-male/) |
| USB cable A-male – microB-male 1.8m | <img src="img/usb.jpg" width="200"> | [Electrokit link](https://www.electrokit.com/en/product/usb-cable-a-male-microb-male-1-8m/) |

## Computer Setup
The chosen IDE for this project is Visual Studio Code with the Pico-w-go extension (with MicroPython firmware) which is used to upload code to the Pico.

## Setup
Donwload Python and Setup VS Code:
1. Download and Install [Python](https://www.python.org/downloads/)
2. Download and Install [Visual Studio Code IDE](https://code.visualstudio.com/download)
3. Install the Pico-w-go extension in Visual Studio Code

Add the MicroPython firmware to the Pico:
1. Download [MicroPython](https://micropython.org/download/)
2. Connect the micro USB end of the cable to the Pico
3. While pressing the BOOTSEL button on the Pico connect the USB cable to your computer
4. If done correctly a new drive should appear called RPI-RP2, insert the uf2 file retrieved when downloading MicroPython into this drive.
5. Wait for the the board to automatically disconnect and reconnect.

## Putting Everything Together
The setup given below is an example of how the different components can be connected.

IMPORTANT THINGS THAT MUST BE CONNECTED PROPERLY
1. Temperature sensor: Ground pin to GND, 3V3(OUT) to Vdd pin and ADC pin to Vout See datasheet for temperature sensor [here](https://www.electrokit.com/uploads/productfile/41011/21942e-2.pdf).
2. LED: GP pin to Anode and Ground pin to Cathode. See datasheet for LED [here](https://www.electrokit.com/uploads/productfile/40307/JSL-502-4030702x.pdf)

Rasberrry Pi Pico W [documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

<img src="img/IoT-Bb-Sketch.png">

## Platform
The choice of platform for this project is Adafruit IO. Adafruit IO is a cloud service with focus on ease of use, it provides a easy way to send data to a server and display it without much programming.

Read more about setting up an Adafruit IO [here](https://learn.adafruit.com/adafruit-io-home-security/adafruit-io-setup).

## Code
SendTemperature is the core function of the program, it sends the temperature to our adafruit IO and calls the SendLED. The sendLED function sends the LED status to adafruit and then depending on the LED status and time constraints calls the sendNotification function which signals the program to send a notification.

https://github.com/jonsch0219/Iot-Project-S23/blob/86fe0c3e9558c0584c30651cdc2d9f4eeeb9386d/src/adafruit.py

The function getTemperature takes a filter_size as parameter which defines how many temperatures the function will take the average of and return as the temperature value. 

https://github.com/jonsch0219/Iot-Project-S23/blob/d48b7796de0d94e5900668648d82ea4feb5a29c0/src/temperature.py

In order to dynamically change the temperature upper bound in the adafruit IO. I created a slider which is controlled by this callback function. 


https://github.com/jonsch0219/Iot-Project-S23/blob/73f7e2fbf9c12e83746824b25d10b1d883acdc48/src/adafruit.py

In the main code the client checks for any interactions with the slider and calls the tempSlider function if there is change in value.

https://github.com/jonsch0219/Iot-Project-S23/blob/b098f8f62e0264f2d285141ba8a120c648edc548/src/main.py








