alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


def encrypt(plain_text, shift):
    result = []
    cypher_text = []

    for eachLetter in plain_text:
        if eachLetter in alphabet:
            index = alphabet.index(eachLetter)
            encrypt = (index + shift) % 26
            cypher_text.append(encrypt)
            newLetter = alphabet[encrypt]
            result.append(newLetter)
    return result


encrypted_code = encrypt(text, shift)
# print(encrypted_code)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


def decrypt(code_text, shift):
    result1 = []
    encrypted_text = []

    for eachLetter in code_text:
        if eachLetter in alphabet:
            index = alphabet.index(eachLetter)
            decrypt = (index - shift) % 26
            encrypted_text.append(decrypt)
            newLetter = alphabet[decrypt]
            result1.append(newLetter)
    return result1


decrypted_code = decrypt(text, shift)
# print(decrypted_code)

# decrypted_code = decrypt(text, shift)
# print(decrypted_code)

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift=shift)
    print(encrypted_code)
elif direction == "decode":
    decrypt(code_text=text, shift=shift)
    print(decrypted_code)
