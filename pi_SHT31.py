from smbus import SMBus
import time
import sys

address = 0x71 #I2C address of SHT31

print("Hello world")

bus = SMBus(1) # 1 indicates /dev/i2c-1



def busWriteQuick(address):
    try:   
        bus.write_quick(address)
        print("DEC address: " + str(address) + " HEX address: " + str(hex(address)))
    except IOError as e:
        print("ERROR" + "DEC address: " + str(address) + " HEX address: " + str(hex(address)))
#     time.sleep(.5)
def scanNext(direction): # blocking
    promptString = ''
    if direction == "u":
        promptString = "UP next or"
    elif direction == "d":
        promptString = "DOWN next or"
    else:
        promptString = "invalid, "

    newDirection = raw_input(promptString + " enter 'u' or 'd' then press enter: ")

    if (newDirection == ""):

        pass
    elif (newDirection == direction):
        print("allready going: " + newDirection)
    else:
        return scanNext(newDirection)

    return direction

initValue = 0
resultString = 'u'

while True:

    busWriteQuick(initValue)
    resultString = scanNext(resultString) #returns only with 'u' or 'd'
    print("*** result: " + resultString)

    if resultString == 'u':
        initValue = initValue +1
    elif resultString == 'd':
        initValue = initValue -1 



    






