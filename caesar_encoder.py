import library as lib

ALPHABET = lib.ALPHABET


def encrypt(input_text, shift):
    input_text = input_text.lower()
    shift = int(shift)
    output_text = ''

    for i in input_text:
        if i in ALPHABET:
            new_index = ALPHABET.index(i) + shift
            output_text += ALPHABET[new_index]
        else:
            output_text += i

    return output_text


def decrypt(input_text, reverse_shift):
    reverse_shift = int(reverse_shift)
    input_text = input_text.lower()
    output_text = ''

    for i in input_text:
        if i in ALPHABET:
            new_index = ALPHABET.index(i) - reverse_shift
            output_text += ALPHABET[new_index]
        else:
            output_text += i

    return output_text
