#!/usr/bin/env python3
# bass_oscill tests whether a speaker can handle frequencies lower than 100 Hertz
# Linux: install SoX with your package manager.
# macOS:
# First install Homebrew (https://brew.sh/) 
# and then SoX using 'brew install sox' in the terminal
# Windows:
# https://github.com/JoFrhwld/FAVE/wiki/Sox-on-Windows
import os
from piano_note_frequencies import keys

duration  = 50 # milliseconds

print("Hertz:")

for i in range(len(keys)):
        note = keys[i][0]
        freq = float(keys[i][1])
        print(note)
        print(freq)
        os.system('play -q -n synth %s sawtooth %s > /dev/null' % (duration/1000, freq))
