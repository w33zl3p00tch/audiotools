#!/usr/bin/env python3
# whitenoise does what it says on the tin
# Linux: install SoX with your package manager.
# macOS:
# First install Homebrew (https://brew.sh/) 
# and then SoX using 'brew install sox' in the terminal
# Windows:
# https://github.com/JoFrhwld/FAVE/wiki/Sox-on-Windows
import os
duration  = 200000 # milliseconds
freq = 1000
os.system('play -q -n synth %s brownnoise %s > /dev/null' % (duration/1000, freq))
