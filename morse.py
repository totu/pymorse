#!/usr/bin/env python3
from libmorse import MORSE_ALPHABET
import os
from time import sleep

if os.name == "nt":
    import winsound
    WINDOWS = True
else:
    WINDOWS = False

FREQ = 1000
UNIT = 110


def convert_text_to_morse(string):
    out = []
    for character in string:
        character = character.upper()
        if character in MORSE_ALPHABET:
            out.append(MORSE_ALPHABET[character])
    # TODO: This needs more thought
    return " ".join(out).replace(" "*3, " "*2)


def convert_morse_to_text(string, dash="-", dot="·"):
    string = string.replace(str(dash), "-").replace(str(dot), "·")

    out = ""
    for word in string.split("  "):
        for character in word.split(" "):
            for letter in MORSE_ALPHABET:
                if MORSE_ALPHABET[letter] == character:
                    out += letter
                    break
        out += " "

    return out.strip()

def play(string):
    dash = "-"
    out = []
    for word in string.split("  "):
        for character in word.split(" "):
            for c in character:
                duration = UNIT
                if c == dash:
                    duration = duration * 3
                out.append((True, duration))
                out.append((False, UNIT))
            out.append((False, UNIT * 3))
        out.append((False, UNIT * 7))

    return out

if __name__ == "__main__":
    x = convert_text_to_morse("tämä on testi")
    out = play(x)
    import wave, struct, random
    obj = wave.open("test.wav", "w")
    obj.setnchannels(1)
    obj.setsampwidth(2)
    obj.setframerate(1000)
    for play, duration in out:
        duration = duration 
        data = struct.pack('<h', play * 15000)
        for _ in range(duration):
            obj.writeframesraw( data )
    # for play, duration in out:
    #     data = struct.pack("<h", 100)
    #     data = struct.pack("<h", 100)
    #     data = struct.pack("<h", 100)
    #     data = struct.pack("<h", 100)
    #     data = struct.pack("<h", 100)
    #     obj.writeframesraw(data)
    
    obj.close()