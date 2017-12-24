from time import sleep
from tqdm import tqdm
import grovepi

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0
grovepi.pinMode(sound_sensor,"INPUT")

# The threshold
threshold_value = 400

# Setup Progress Bar
pbar = tqdm(["HOTOKE", "NO", "KAO"])
num = 0

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

        print("sensor_value = %d" %sensor_value)
        sleep(0.1)

    except IOError:
        print("Error")
