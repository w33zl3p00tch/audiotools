#!/usr/bin/env python3
# helps you tune your violin.
keys = [
        ["g", "195.998"],
        ["d'", "293.665"],
        ["a'", "440.000"],
        ["e''", "659.255"],
]
import os
import time
duration  = 4000 # milliseconds

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
