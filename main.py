import os
from datetime import datetime

chimeHours = [8, 11, 20]
chimeMin = 0
resetHour = 23
is_played = False
while True:
    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute

    for hour in chimeHours:
        if currentHour == hour and currentMin == chimeMin and not is_played:
            print("Playing a chime for " + str(hour) + ":00")
            is_played = True
            # os.system("aplay home/westminster-chimes.wav")
            for i in range(hour):
                print("Test")
                # os.system("aplay home/funeral-bell.wav")
    if currentHour == resetHour:
        print("Rebooting Now")
        # os.system("sudo reboot -n")
    if not (currentHour in chimeHours) or currentMin != chimeMin:
        is_played = False