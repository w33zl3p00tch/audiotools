#!/usr/bin/env python3
"""
once it's stable, speakercheck will test the noise pressure level of loudspeakers.
Work in progress
"""
# Linux: install SoX with your package manager.
# macOS:
# First install Homebrew (https://brew.sh/)
# and then SoX using 'brew install sox' in the terminal
# Windows:
# https://github.com/JoFrhwld/FAVE/wiki/Sox-on-Windows
import os
import time

duration  = 600 # milliseconds

print("Hertz:")

os.system('sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber --buffer $((96000*2*10)) ~/soxrecording1.wav trim 0 20 &')

for i in range(0, 15000, 40):
    print(i)
    os.system('play -q -n synth %s sin %s & > /dev/null' % (duration/1000, i))
    time.sleep(0.3)
