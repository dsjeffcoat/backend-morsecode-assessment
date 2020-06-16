#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Morse code decoder

https://www.codewars.com/kata/decode-the-morse-code/python
https://www.codewars.com/kata/decode-the-morse-code-advanced/python


When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is.
And in fact different operators would transmit at different speed.
An amateur person may need a few seconds to transmit a single character,
a skilled professional can transmit 60 words per minute,
and robotic transmitters may go way faster.

OK FOR REAL??  60 WPM??
https://morsecode.scphillips.com/translator.html

For this kata we assume the message receiving is performed automatically by
the hardware that checks the line periodically, and if the line is connected
(the key at the remote station is down), 1 is recorded, and if the line is
not connected (remote key is up), 0 is recorded. After the message is fully
received, it gets to you for decoding as a string containing only
symbols 0 and 1.
"""

# This dictionary is supplied within the Codewars test suite.
MORSE_CODE = {
    '.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
    '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
    '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
    '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
    '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
    '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
    '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
    '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
    '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C',
    '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$',
    '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(',
    '---..': '8', '...--': '3'
}


def find_mult(bits):
    """Finds least amount of occurrences of 0 or 1"""
    smallest_zeros = len(
        min([group for group in bits.split('1') if group != '']))
    smallest_ones = len(
        min([group for group in bits.split('0') if group != '']))
    return min(smallest_zeros, smallest_ones)


def decode_bits(bits):
    """Translate a string of 1's & 0's to dots and dashes"""
    unit = find_mult(bits)
    stmt = bits.replace('0' * unit * 7, '   ').replace('0' *
                                                       unit * 3, ' ')
    morse_code = stmt.replace(
        '1' * unit * 3, '-').replace('1' * unit, '.').replace('0' * unit, '')
    return morse_code


def decodeMorse(morse_code):
    """Translates a string of dots and dashes to human readable text"""
    decoded = ''
    morse_words = morse_code.split('   ')
    for morse_word in morse_words:
        for morse_char in morse_word.split():
            decoded += MORSE_CODE[morse_char]
        decoded += ' '
    print(len(decoded.strip()))
    return decoded.strip()


# print(find_mult('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))
print(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
# print('.... . -.--   .--- ..- -.. .')
# print(decodeMorse('.... . -.--   .--- ..- -.. .'))
