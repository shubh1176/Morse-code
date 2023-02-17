# Morse-code
Morse Code Encryptor and Decryptor
Morse code is a system of communication that uses a series of dots, dashes, and spaces to represent letters, numbers, and other characters. It was developed in the early 1830s by Samuel Morse and Alfred Vail for use with telegraph machines. Morse code can be transmitted over long distances using only a simple on-off signal, making it a valuable communication tool for use in situations where other forms of communication are not possible.

In Morse code, each letter, number, and symbol is represented by a unique sequence of dots and dashes, which are typically written as short and long marks (e.g., "." and "-"). The length of a dash is usually three times longer than that of a dot. The letters and numbers are grouped into words with spaces between each word.
Although Morse code is no longer widely used as a primary means of communication, it is still used by amateur radio operators, the military, and in other niche applications. Morse code has also had a lasting impact on the development of digital communication technology, as it was one of the first systems to use a binary code to represent information.

# ALGORITHM :
Every character in the English language is substituted by a series of ‘dots’ and ‘dashes’ or sometimes just singular ‘dot’ or ‘dash’ and vice versa.

The code uses a dictionary called MORSE_CODE to represent the Morse code chart, where each letter, number, and symbol is mapped to a unique sequence of dots and dashes.

The encrypt() function takes a message as input and returns the encrypted message as a string of dots and dashes, separated by spaces. The function looks up the Morse code for each character in the message and adds it to the cipher string. A space is added after each character's Morse code to indicate the start of a new character.

The decrypt() function takes a Morse code message as input and returns the decrypted message as a string. The function reads each character of the Morse code message and checks if it is a space. If it is a space, the function checks if there are one or two spaces. One space indicates a new character, and two spaces indicate a new word. The function then looks up the character corresponding to the Morse code in the dictionary and adds it to the decipher string.

The main() function is the driver function that allows the user to choose whether they want to encrypt a message or decrypt a Morse code message. If the user selects encryption, the function prompts the user to enter the message and calls the encrypt() function. If the user selects decryption, the function prompts the user to enter the Morse code message and calls the decrypt() function.




