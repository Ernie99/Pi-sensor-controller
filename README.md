# Raspberry Pi controller for i2c sensors, Python code

## Tested on *RASPBIAN JESSIE* , *Raspberry Pi 2 Model B*, *Python 3*

### installed:
* quick2wire
* i2c-tools

### Program to:
* Interface with i2c bus for test and development
* Read data from sensors
* Control relays over USB serial port

### Sensors supported:
* Sensirion SHT3x temperature and humidity sensor (i2c)
* Maxim DS3231 (i2c) (work in progress)
* other temperature and humidity sensors (work in progress)

### external peripherals:
* Synaccess Remote Power Switch NP-02
* FTDI Chipi-X RS232 DB9 Cable

## Develoment envirment

## Host:
Code is written on host machine and sent over **scp** when file changes. The **whenchanged** python utility is run from a simple python script. When modification is detected, bash script is executed that runs a **scp** command using the **sshpass** command. See:
https://github.com/joh/when-changed

## RasPi:
Like the host, **whenchanged** is also installed, and a scrip is run to detect when a new file arrives, and runs that file.
