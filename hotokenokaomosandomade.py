from time import sleep
import grovepi
import requests

# Maker Webhooks Name
EVENT = "RAIJIN"
# Maker Webhooks Key
KEY = ""


# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0
grovepi.pinMode(sound_sensor,"INPUT")

# Connect the Grove LED to digital port D2
led = 2
grovepi.pinMode(led,"OUTPUT")
grovepi.digitalWrite(led,0)

# The threshold
threshold_value = 400

# Setup Progress
num = 0
hotoke = True

def nidoarukotohasandoaru(){
    url = "https://maker.ifttt.com/trigger/" + EVENT + "/with/key/" + KEY
    requests.post(url=url)
}

while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)
        if num == 1:
            grovepi.digitalWrite(led,1)
            print("HOTOKE NO")

        if num == 2:
            grovepi.digitalWrite(led,hotoke)
            hotoke = not(hotoke)
            print("KAO MO")

        if num >= 3 :
            print("SANDOMADE\n\r")
            nidoarukotohasandoaru()
            break

        if sensor_value > threshold_value:
            num += 1

        print("sensor_value = %d" %sensor_value)
        sleep(0.2)

    except KeyboardInterrupt:
        grovepi.digitalWrite(led,0)
        break
    except IOError:
        print ("Error")
