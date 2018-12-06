IGNITION_PIN_NUM = 0
EXPORT_PATH = '/sys/class/gpio/export'

def getGpioPath(pinNum, prop):
    # this will return /sys/class/gpio/gpio0/direction
    return '/sys/class/gpio/gpio%d/%s' % (pinNum, prop)

def exportPin(pinNum):
    with open(EXPORT_PATH, "w") as export:
        export.write(pinNum)

def setPinAsOutput(pinNum):
    path = getGpioPath(pinNum, 'direction')
    with open(path, 'w') as output:
        output.write("out")

def turnOn(pinNum):
    path = getGpioPath(pinNum, 'value')
    # ex: path = '/sys/class/gpio/gpio10/value'
    with open(path, 'w') as pin:
        pin.write("1")

def turnOff(pinNum):
    path = getGpioPath(pinNum, 'value')
    with open(path, 'w') as output:
        output.write("0")
    

# export the pin once so that it's
# available for use when the rapsberry pi
# turns on
exportPin(IGNITION_PIN_NUM)
setPinAsOutput(IGNITION_PIN_NUM)
# never ending loop
while True:
    # turn on the ignition
    turnOn(IGNITION_PIN_NUM)

    # wait for 60 seconds
    sleep(10)
    
    # turn it back off
    turnOff(IGNITION_PIN_NUM)

    # wait for 60 seconds
    sleep(10)
