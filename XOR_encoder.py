def crypt(input_text, key):  # Use ASCII please
    key = int(key)

    output_string = ''

    for i in input_text:

        crypt_symbol = ord(i) ^ key
        symbol = chr(crypt_symbol)

        output_string += symbol

    print(output_string)
    return output_string
