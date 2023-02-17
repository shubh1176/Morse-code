# Dictionary representing morse code for
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

# Function to encrypt the string
# according to the morse code chart
def encrypt(text):
    cipher = ''
    for letters in text:
        if letters != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE[letters] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

# Function to decrypt the string
# from morse to english
def decrypt(text):

    # extra space added at the end to access the
    # last morse code
    text += ' '

    decipher = ''
    ciphertext = ''
    for letters in text:
        # checks for space
        if (letters != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            ciphertext += letters

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE.keys())[list(MORSE_CODE
                .values()).index(ciphertext)]
                ciphertext = ''

    return decipher

# Hard-coded driver function to run the program
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