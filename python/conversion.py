#!/usr/bin/python3
# Conversion functions for the NATO Phonetic Alphabet.

# To save a lot of typing the code words are presented here
# as a dict, but feel free to change this if you'd like.
ALPHANUM_TO_NATO = {
    "A": "ALFA",
    "B": "BRAVO",
    "C": "CHARLIE",
    "D": "DELTA",
    "E": "ECHO",
    "F": "FOXTROT",
    "G": "GOLF",
    "H": "HOTEL",
    "I": "INDIA",
    "J": "JULIETT",
    "K": "KILO",
    "L": "LIMA",
    "M": "MIKE",
    "N": "NOVEMBER",
    "O": "OSCAR",
    "P": "PAPA",
    "Q": "QUEBEC",
    "R": "ROMEO",
    "S": "SIERRA",
    "T": "TANGO",
    "U": "UNIFORM",
    "V": "VICTOR",
    "W": "WHISKEY",
    "X": "XRAY",
    "Y": "YANKEE",
    "Z": "ZULU",
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "TREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINER",
}

def transmit(message: str) -> str:
    """
    Convert a message to a NATO code word transmission.
    """
    values_punctuation = [' ', ',', '.', '-', '!', '_', ':']
    key = ''

    for i in values_punctuation:
        row_line = message.replace(i, key)

    list_word = list(row_line)

    for i in list_word:
        for k in ALPHANUM_TO_NATO.keys():
            if i == k:
                print(ALPHANUM_TO_NATO[k], end=' ')
    print()


def receive(transmission: str) -> str:
    """
    Convert a NATO code word transmission to a message.
    """
    list_string = transmission.split(' ')
    
    for i in list_string:
        for key, value in ALPHANUM_TO_NATO.items():
            if i == value:
                print(key, end='')
    print()