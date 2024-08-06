import os
from datetime import datetime

CHIME_HOURS = [9, 12, 17]  # If you add an hour make sure to add a corresponding minute
CHIME_MINS = [0, 2, 58]  # CHIME_MINS & CHIME_HOURS should be the same length
RESET_HOUR = 23
VOLUME = 100  # Set the volume (out of 100)

WESTMINSTER_FILE_PATH = "westminster-chimes.wav"
BELL_CHIME_FILE_PATH = "funeral-bell.wav"

SOUND_DEVICE = "hdmi:CARD=vc4hdmi1,DEV=0"

output = "Church Bells are set for "

def formatTime(min):
    if (min == 0):
        return "00"

for i in range(len(CHIME_HOURS)):
    hour = CHIME_HOURS[i]
    min = CHIME_MINS[i]

    output += str(hour) + ":"

    # Properly formats
    if min == 0:
        output += "00"
    if i != len(CHIME_HOURS) - 1:
        output += ", "
print(output)

is_played = False
while True:
    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute
    currentSec = now.second

    for i in range(len(CHIME_HOURS)):
        hour = CHIME_HOURS[i]
        min = CHIME_MINS[i]
        if currentHour == hour and currentMin == min and not is_played:
            print("Playing a chime for " + str(hour) + ":" + str(min))
            is_played = True

            os.system("amixer set Master " + str(VOLUME) + "%")
            os.system("aplay --device " + SOUND_DEVICE + " " + WESTMINSTER_FILE_PATH)
            os.system("aplay --device " + SOUND_DEVICE + " " + WESTMINSTER_FILE_PATH)

            # Since datetime works on a 24 hour clock, the hour has to be converted to the 12 hour clock for the chimes
            numRepeat = hour % 12
            if numRepeat == 0:
                numRepeat = 12

            for i in range(numRepeat):
                os.system("aplay --device " + SOUND_DEVICE + " " + BELL_CHIME_FILE_PATH)
    
    if currentHour == RESET_HOUR and currentMin == 0 and currentSec == 0:  # So that the Raspberry Pi is not just constantly on
        print("Rebooting Now")
        # os.system("sudo reboot -n")
    if not (currentHour in CHIME_HOURS) or not (currentMin in CHIME_MINS):
        is_played = False