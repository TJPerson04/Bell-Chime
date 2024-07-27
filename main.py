import os
from datetime import datetime

CHIME_HOURS = [8, 12, 20]
CHIME_MIN = 23
RESET_HOUR = 23

WESTMINSTER_FILE_PATH = "westminster-chimes.wav"
BELL_CHIME_FILE_PATH = "funeral-bell.wav"

SOUND_DEVICE = "hdmi:CARD=vc4hdmi1,DEV=0"

is_played = False
while True:
    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute

    for hour in CHIME_HOURS:
        if currentHour == hour and currentMin == CHIME_MIN and not is_played:
            print("Playing a chime for hour: " + str(hour) + " and min: " + str(CHIME_MIN))
            is_played = True
            os.system("aplay --device " + SOUND_DEVICE + " " + WESTMINSTER_FILE_PATH)

            # Since datetime works on a 24 hour clock, the hour has to be converted to the 12 hour clock for the chimes
            numRepeat = hour % 12
            if numRepeat == 0:
                numRepeat = 12

            for i in range(numRepeat):
                os.system("aplay --device " + SOUND_DEVICE + " " + BELL_CHIME_FILE_PATH)
    
    if currentHour == RESET_HOUR and currentMin == 0:  # So that the Raspberry Pi is not just constantly on
        print("Rebooting Now")
        # os.system("sudo reboot -n")
    if not (currentHour in CHIME_HOURS) or currentMin != CHIME_MIN:
        is_played = False