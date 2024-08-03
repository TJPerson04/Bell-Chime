import os

FILE_PATH = "westminster-chimes.wav"
SOUND_DEVICE = "hw:CARD=Headphones,DEV=0"

while True:
    os.system("aplay --device " + SOUND_DEVICE + " " + FILE_PATH)