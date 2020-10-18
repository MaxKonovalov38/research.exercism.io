"""
Conversion functions for the NATO Phonetic Alphabet.
"""

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
    list_word = list(message)

    for i in list_word:
        for k in ALPHANUM_TO_NATO.keys():
            if i == k:
                print(ALPHANUM_TO_NATO[k], end=' ')


def receive(transmission: str) -> str:
    """
    Convert a NATO code word transmission to a message.
    """
    pass  # <- implement your function


def redacting_str(row_line: str) -> str:
    '''
    Функция redacting_str() редактирует строку,
    убрав из неё знаки препинания и пробелы.
    :param row_line - необработанная строка
    '''
    values_punctuation = [' ', ',', '.', '_', '!']
    key = ''

    for i in values_punctuation:
        row_line = row_line.replace(i, key)

    return row_line


def main():
    '''
    Функция main() принимает от пользователя сообщение, а
    также режим кодировать/раскодировать (E/D).
    '''
    start_message = input("Write the message: ").upper()
    crypt_mode = input("[E]ncrypt|[D]ecrypt: ").upper()

    if crypt_mode == 'E':
        row_message = redacting_str(start_message)
        transmit(row_message)
        print() # Добавляет \n
    elif crypt_mode == 'D':
        receive(start_message)
    else:
        print("Error: parametr is not found!!!")
        raise SystemExit


if __name__ == '__main__':
    main()