#!/usr/bin/env python3
from libmorse import MORSE_ALPHABET
import os
from time import sleep
import wave
import struct
import tempfile
from playsound import playsound

FREQ = 2000
UNIT = 90


def convert_text_to_morse(string):
    out = []
    for character in string:
        character = character.upper()
        if character in MORSE_ALPHABET:
            out.append(MORSE_ALPHABET[character])
    # TODO: This needs more thought
    return " ".join(out).replace(" " * 3, " " * 2)


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


def _create_output(string):
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


def _make_wave(out, filename):
    obj = wave.open(f"{filename}", "w")
    obj.setnchannels(1)
    obj.setsampwidth(2)
    obj.setframerate(FREQ)

    for play, duration in out:
        duration = duration
        for _ in range(duration):
            data = struct.pack("<h", play * 0x7FFF)
            obj.writeframesraw(data)
            data = struct.pack("<h", play * -0x7FFF)
            obj.writeframesraw(data)

    obj.close()


def play_string(string):
    morse = convert_text_to_morse(string)
    play_morse(morse)


def play_morse(morse, filename=None, play=True):
    out = _create_output(morse)
    context = tempfile.NamedTemporaryFile()

    # Create correct context
    if filename:
        context = open(filename, "wb")
    else:
        filename = context.name

    with context as ctx:
        _make_wave(out, filename)
        if play:
            playsound(filename)


def create_wav(string, filename, morse=False):
    if not morse:
        string = convert_text_to_morse(string)

    play_morse(string, filename, play=False)


if __name__ == "__main__":
    # play_string("sos")
    morse = convert_text_to_morse("sos")
    create_wav("sos", "sos.wav", morse=False)
