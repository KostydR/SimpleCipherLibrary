import library as lib

ALPHABET = lib.ALPHABET
REVERSE_ALPHABET = lib.REVERSE_ALPHABET


def crypt(input_text):  # for decrypt just use it again
    input_text = input_text.lower()
    output_text = ''

    for i in input_text:
        if i in ALPHABET:
            index = ALPHABET.index(i)
            new_symbol = REVERSE_ALPHABET[index]
            output_text += new_symbol
        else:
            output_text += i

    return output_text
