import os
from datetime import datetime

CHIME_HOURS = [8, 12, 20]
CHIME_MIN = 15
RESET_HOUR = 23

WESTMINSTER_FILE_PATH = "home/westminster-chimes.wav"
BELL_CHIME_FILE_PATH = "home/funeral-bell.wav"

is_played = False
while True:
    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute

    for hour in CHIME_HOURS:
        if currentHour == hour and currentMin == CHIME_MIN and not is_played:
            print("Playing a chime for hour: " + str(hour) + " and min: " + str(CHIME_MIN))
            is_played = True
            os.system("aplay " + WESTMINSTER_FILE_PATH)
            for i in range(hour):
                os.system("aplay " + BELL_CHIME_FILE_PATH)
    if currentHour == RESET_HOUR and currentMin == 0:  # So that the Raspberry Pi is not just constantly on
        print("Rebooting Now")
        # os.system("sudo reboot -n")
    if not (currentHour in CHIME_HOURS) or currentMin != CHIME_MIN:
        is_played = False