from flask import Flask, render_template
import RPi.GPIO as GPIO
import subprocess
import atexit
import time
import thread
import re
app = Flask(__name__)

selected = []
pins = [17,18,27,22,23,24]
lastValve = 18

@app.route('/garden')
def garden():
    return render_template('garden.html')

@app.route('/water/<valve>/<length>')
def controls(valve,length):
    global selected
    selected = re.findall('..',valve)
    thread.start_new_thread(water,(selected,length))
    return "Watering... "

def water(valve,length):
    global lastValve
    setupGPIO()
    GPIO.output(lastValve,GPIO.LOW)
    for i in valve:
        GPIO.output(int(i),GPIO.HIGH)
        time.sleep(float(length))
        GPIO.output(int(i),GPIO.LOW)
        lastValve = int(i)

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for i in pins:
        GPIO.setup(i, GPIO.OUT)    

#Sets all GPIOs to LOW on exit
def exit_handler():
    setupGPIO()
    for i in pins:
       	GPIO.output(int(i), GPIO.LOW)
    GPIO.cleanup()
    
atexit.register(exit_handler)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

