from time import sleep
from tqdm import tqdm
import liblo
import grovepi

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0
grovepi.pinMode(sound_sensor,"INPUT")

# The threshold
threshold_value = 400

# Setup OSC Client
target = liblo.Address("localhost",5005)

# Setup Progress Bar
pbar = tqdm(["HOTOKE", "NO", "KAO"])
num = 0
hotoke = ["HOTOKE", "NO", "KAO"]

while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)

        if num >= 3 :
            print("BYE\n\r")
            break

        if sensor_value > threshold_value:
            pbar.update()
            num += 1
            liblo.send(target, "/foo/bar", num, hotoke[num-1])

        print("sensor_value = %d" %sensor_value)
        sleep(0.2)

    except IOError:
        print("Error")
