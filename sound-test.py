import os

FILE_PATH = "westminster-chimes.wav"
SOUND_DEVICE = "sysdefault"

while True:
    os.system("aplay --device " + SOUND_DEVICE + " " + FILE_PATH)