#!/usr/bin/env python3
# bass_oscill tests whether a speaker can handle frequencies lower than 100 Hertz
# Linux: install SoX with your package manager.
# macOS:
# First install Homebrew (https://brew.sh/) 
# and then SoX using 'brew install sox' in the terminal
# Windows:
# https://github.com/JoFrhwld/FAVE/wiki/Sox-on-Windows
import os
duration  = 50 # milliseconds

keys = [
        ["Csub", "16.3516"],
        ["C#/Db", "17.3239"],
        ["D0", "18.3540"],
        ["D#/Eb", "19.4454"],
        ["E", "20.6017"],
        ["F", "21.8268"],
        ["F#/Gb", "23.1247"],
        ["G", "24.4997"],
        ["G#/Ab", "25.9565"],
        ["A", "27.5000"],
        ["A#/Bb", "29.1352"],
        ["B", "30.8677"],
        ["C", "32.7032"],
        ["D", "36.7081"],
        ["D#/Eb", "38.8909"],
        ["E", "41.2034"],
        ["F", "43.6535"],
        ["F#/Gb", "46.2493"],
        ["G", "48.9994"],
        ["G#/Ab", "51.9131"],
        ["A", "55.0000"],
        ["A#/Bb", "58.2705"],
        ["B", "61.7354"],
        ["C", "65.4064"],
        ["C#/Db", "69.2957"],
        ["D", "73.4162"],
        ["D#/Eb", "77.7817"],
        ["E", "82.4069"],
        ["F", "87.3071"],
        ["F#/Gb", "92.4986"],
        ["G", "97.9989"],
        ["G#/Ab", "103.8260"],
        ["A", "110.0000"],
        ["A#/Bb", "116.541"],
        ["B", "123.471"],
        ["c", "130.813"],
        ["c#/db", "138.591"],
        ["d","146.832"],
        ["d#/eb", "155.563"],
        ["e", "164.814"],
        ["f", "174.614"],
        ["f#/gb", "184.997"],
        ["g", "195.998"],
        ["g#/ab", "207.652"],
        ["a", "222.000"],
        ["a#/bb", "233.082"],
        ["b", "246.942"],
        ["c'", "261.626"],
        ["c#'/db'", "277.183"],
        ["d'", "293.665"],
        ["d#'/eb'", "311.127"],
        ["e'", "329.628"],
        ["f'", "349.228"],
        ["f#'/gb'", "369.994"],
        ["g'", "391.995"],
        ["g#'/ab'", "415.305"],
        ["a'", "440.000"],
        ["a#'/bb'", "466.164"],
        ["b'", "493.883"],
        ["c''", "523.251"],
        ["c#''/db''", "554.365"],
        ["d''", "587.330"],
        ["d#''/eb''", "622.254"],
        ["e''", "659.255"],
        ["f''", "698.456"],
        ["f#''/gb''", "739.989"],
        ["g''", "783.991"],
        ["g#''/ab''", "830.609"],
        ["a''", "880.000"],
        ["a#''/bb''", "932.328"],
        ["b''", "987.767"],
        ["c'''", "1046.500"],
        ["c#'''/db'''", "1108.73"],
        ["d'''", "1174.66"],
        ["e'''", "1318.51"],
        ["f'''", "1396.91"],
        ["f#'''/gb'''", "1479.98"],
        ["g'''", "1567.98"],
        ["g#'''/ab'''", "1661.22"],
        ["a'''", "1760.000"],
        ["a#'''/bb'''", "1864.66"],
        ["b'''", "1975.53"],
        ["c'''''", "2093.00"],
        ["c#'''''/db'''''", "2217.46"],
        ["d'''''", "2349.32"],
        ["d#'''''/eb'''''", "2489.02"],
        ["e'''''", "2637.02"],
        ["f'''''", "2793.83"],
        ["f#'''''/gb'''''", "2959.96"],
        ["g''''", "3135.96"],
        ["g#'''''/bb'''''", "3322.44"],
        ["a''''", "3520.00"],
        ["a#'''''/bb'''''", "3729.31"],
        ["b'''''", "3951.07"],
        ["c'''''", "4186.01"],
        ["c#'''''/db'''''", "4434.92"],
        ["d''''", "4698.64"],
        ["d#'''''/eb'''''", "4978.03"],
        ["e'''''", "5274.04"],
        ["f'''''", "5587.65"]
        
]


print("Hertz:")

for i in range(len(keys)):
        note = keys[i][0]
        freq = float(keys[i][1])
        print(note)
        print(freq)
        os.system('play -q -n synth %s trapezium %s > /dev/null' % (duration/1000, freq))
