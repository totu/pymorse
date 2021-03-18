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

    for play, duration in out:
        if play: 
            winsound.Beep(FREQ, duration)
        else:
            sleep(duration//1000)


if __name__ == "__main__":
    x = convert_text_to_morse("tämä on testi")
    play(x)