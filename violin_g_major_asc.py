#!/usr/bin/env python3
# Linux: install SoX with your package manager.
# macOS:
# First install Homebrew (https://brew.sh/) 
# and then SoX using 'brew install sox' in the terminal
# Windows:
# https://github.com/JoFrhwld/FAVE/wiki/Sox-on-Windows
import os
import time
from violin_g_major import keys
duration  = 800 # milliseconds

print("Hertz:")
while True:
    for i in range(len(keys)):
        note = keys[i][0]
        freq = float(keys[i][1])
        print(note)
        print(freq)
        os.system('play -q -n synth %s trapezium %s > /dev/null' % (duration/1000, freq))
    time.sleep(2)

    for i in range(len(keys)):
        cur = len(keys)-i-1
        note = keys[i][0]
        print(cur)
        print(note)
        freq = float(keys[cur][1])
        print(note)
        print(freq)
        os.system('play -q -n synth %s trapezium %s > /dev/null' % (duration/1000, freq))
    time.sleep(2)
