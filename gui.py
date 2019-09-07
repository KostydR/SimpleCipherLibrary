import easygui as eg
import caesar_encoder as ce
import atbash_encoder as ae
import XOR_encoder as Xe

answer = eg.buttonbox('What cipher you need today, sir?', choices=['Atbash', 'Caesar', 'XOR'])

if answer == 'Caesar':
    caesar_mode = eg.buttonbox('Encrypt or decrypt', choices=['encrypt', 'decrypt'])

    if caesar_mode == 'encrypt':
        input_text = str(eg.enterbox('write some text pls'))
        shift = int(eg.enterbox('enter shift (0-25)'))

        encrypted_text = ce.encrypt(input_text, shift)
        eg.textbox('Encrypted text, sir', text=encrypted_text)
    else:
        input_text = str(eg.enterbox('enter text for decryption'))
        reverse_shift = int(eg.enterbox('enter shift (0-25)'))

        decrypted_text = ce.decrypt(input_text, reverse_shift)
        eg.textbox('Decrypted text, sir', text=decrypted_text)
elif answer == 'Atbash':
    input_text = str(eg.enterbox('enter text for operation'))

    crypt_text = ae.crypt(input_text)
    eg.textbox('Crypted text, sir', text=crypt_text)
else:
    input_text = str(eg.enterbox('enter text for operation (only ascii symbols)'))
    key = int(eg.enterbox('Enter a key (Only integral accepted)'))
    print(input_text)
    print(key)

    crypt_text = Xe.crypt(input_text, key)
    eg.textbox('Crypted text, sir', text=crypt_text)
