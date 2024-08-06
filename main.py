import os
from datetime import datetime

CHIME_HOURS = [8, 11, 17]
CHIME_MIN = 58
RESET_HOUR = 23
VOLUME = 60  # Set the volume (out of 100)

WESTMINSTER_FILE_PATH = "westminster-chimes.wav"
BELL_CHIME_FILE_PATH = "funeral-bell.wav"

SOUND_DEVICE = "hdmi:CARD=vc4hdmi1,DEV=0"

output = "Church Bells are set for hours: "

for hour in CHIME_HOURS:
    output += str(hour)
    output += " "
print(output)

is_played = False
while True:
    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute
    currentSec = now.second

    for hour in CHIME_HOURS:
        if currentHour == hour and currentMin == CHIME_MIN and not is_played:
            print("Playing a chime for hour: " + str(hour) + " and min: " + str(CHIME_MIN))
            is_played = True

            os.system("amixer set Master " + VOLUME + "%")
            os.system("aplay --device " + SOUND_DEVICE + " " + WESTMINSTER_FILE_PATH)
            os.system("aplay --device " + SOUND_DEVICE + " " + WESTMINSTER_FILE_PATH)

            # Since datetime works on a 24 hour clock, the hour has to be converted to the 12 hour clock for the chimes
            numRepeat = hour % 12 + 1  # + 1 b/c bell playing 2 minutes before actual hour
            if numRepeat == 0:
                numRepeat = 12

            for i in range(numRepeat):
                os.system("aplay --device " + SOUND_DEVICE + " " + BELL_CHIME_FILE_PATH)
    
    if currentHour == RESET_HOUR and currentMin == 0 and currentSec == 0:  # So that the Raspberry Pi is not just constantly on
        print("Rebooting Now")
        # os.system("sudo reboot -n")
    if not (currentHour in CHIME_HOURS) or currentMin != CHIME_MIN:
        is_played = False