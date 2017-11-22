#!/usr/bin/env python3
# bass_oscill tests whether a speaker can handle frequencies lower than 100 Hertz
# Linux: install SoX with your package manager.
# macOS:
# First install Homebrew (https://brew.sh/) 
# and then SoX using 'brew install sox' in the terminal
# Windows:
# https://github.com/JoFrhwld/FAVE/wiki/Sox-on-Windows
import os
duration  = 500 # milliseconds

print("Hertz:")

for i in range(0, 100):
    for j in range(0, 100, 5):
        print(j)
        os.system('play -q -n synth %s sin %s > /dev/null' % (duration/1000, j))
    for k in range(0, 100, 5):
        print(k)
        os.system('play -q -n synth %s sin %s > /dev/null' % (duration/1000, 100-k))
