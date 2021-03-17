#!/usr/bin/env python3
from libmorse import MORSE_ALPHABET


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

