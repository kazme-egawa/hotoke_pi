from time import sleep
import grovepi

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0
grovepi.pinMode(sound_sensor,"INPUT")

# Connect the Grove LED to digital port D2
led = 2
grovepi.pinMode(led,"OUTPUT")
grovepi.digitalWrite(led,0)

# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND
relay = 4
grovepi.pinMode(relay,"OUTPUT")

# The threshold
threshold_value = 400

# Setup Progress
num = 0
hotoke = True

while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)
        if num == 1:
            grovepi.digitalWrite(led,1)
            print("HOTOKE NO")

        if num == 2:
            grovepi.digitalWrite(led,hotoke)
            hotoke = !hotoke
            print("KAO MO")

        if num >= 3 :
            print("SANDOMADE\n\r")

            # switch on for 5 seconds
            grovepi.digitalWrite(relay,1)
            print ("on")
            sleep(10)

            # switch off for 5 seconds
            grovepi.digitalWrite(relay,0)
            print ("off")
            sleep(5)
            break

        if sensor_value > threshold_value:
            pbar.update()
            num += 1

        print("sensor_value = %d" %sensor_value)
        sleep(0.2)

    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        grovepi.digitalWrite(led,0)
        break
    except IOError:
        print ("Error")
