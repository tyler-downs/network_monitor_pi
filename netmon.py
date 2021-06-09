import subprocess as sp
import time 
import RPi.GPIO as gpio

GPIO_PIN = 21
cmd = ['ping', '-c', '1', '-w', '1', '8.8.8.8']


def setupPin(pin):
    gpio.setmode(gpio.BCM)
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, False)

def led_on(pin):
    gpio.output(pin, True)

def led_off(pin):
    gpio.output(pin, False)

def write_to_file(message):
    f = open("network_outage_history.csv", "a")
    f.write(message)
    f.close()

def main():
    PIN = 21
    setupPin(PIN)
    ledOn = False
    f = open("network_outage_history.csv", "w+")
    f.write("start,end\n")
    f.close()
    
    try:
        while True:
            p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
            out, err = p.communicate()
            if "1 received" in str(out):
                if ledOn:
                    led_off(PIN)
                    ledOn = False
                    message = "{}\n".format(time.time())
                    write_to_file(message)
                print(".")
            else:
                print("Internet connection down")
                if not ledOn:
                    led_on(PIN)    
                    ledOn = True
                    message = "{},".format(time.time())
                    write_to_file(message) 
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...") 

if __name__ == "__main__":
    main()
