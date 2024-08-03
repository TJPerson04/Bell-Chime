import os

FILE_PATH = "westminster-chimes.wav"
SOUND_DEVICE = "hdmi:CARD=vc4hdmi1,DEV=0"

while True:
    os.system("aplay --device " + SOUND_DEVICE + " " + FILE_PATH)