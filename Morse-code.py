# Dictionary representing morse code 
MORSE_CODE = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 
'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-','U':'..-', 
'V':'...-','W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.','f':'..-.', 'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-',
'l':'.-..', 'm':'--', 'n':'-.', 
'o':'---', 'p':'.--.', 'r':'--.-',
'r':'.-.', 's':'...', 't':'-',
'u':'..-', 'v':'...-', 'w':'.--',
'x':'-..-', 'y':'-.--', 'z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-'}


# from english to morse code
def encrypt(text):
    cipher = ''
    for letters in text:
        if letters != ' ':

            cipher += MORSE_CODE[letters] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


# morse code to english
def decrypt(text):

    # extra space added at the end to access the
    # last morse code
    text += ' '

    deciphertext = ''
    ciphertext = ''
    for letters in text:
        # checks for space
        if (letters != ' '):

            # counter to keep count of space
            i = 0

            ciphertext += letters

        # case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :

                # adding space to separate words
                deciphertext += ' '
            else:

                
                deciphertext += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(ciphertext)]
                ciphertext = ''

    return deciphertext

def main():
    print("1. encrypt the message")
    print("2. decrypt the morse code")
    a = int(input("enter your choice: \n"))
    if a == 1:
        message1 = input("enter your message: ") 
        print(encrypt(message1))
    if a == 2:
        code1 = input("enter the morse code: ")
        print(decrypt(code1))

# Executes the main function
if __name__ == '__main__':
    main()