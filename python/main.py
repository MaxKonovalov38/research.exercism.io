#!/usr/bin/python3
import conversion

def main():
    '''
    Функция main() принимает от пользователя сообщение, а
    также режим кодировать/раскодировать (E/D).
    '''
    start_message = input("Write the message: ").upper()
    crypt_mode = input("[E]ncrypt|[D]ecrypt: ").upper()

    if crypt_mode == 'E':
        conversion.transmit(start_message)
    elif crypt_mode == 'D':
        conversion.receive(start_message)
    else:
        print("Error: parametr is not found!!!")
        raise SystemExit


if __name__ == '__main__':
    main()