keyValue = 0
while keyValue <= 0:
    keyValue = int(input("Please enter key value: ")) % 26
letters = "abcdefghijklmnopqrstuvwxyz"


def encrypt():
    plaintext = input("Please enter plain text: ")
    ciphertext = ""
    for x in plaintext:
        for y in letters:
            if x == y:
                ciphertext += letters[(letters.index(y) + keyValue) % 26]
    print("Cipher text: " + ciphertext)


def decrypt():
    ciphertext = input("Please enter cipher text: ")
    plaintext = ""
    for x in ciphertext:
        if x.isspace():
            plaintext += " "
        for y in letters:
            if x == y:
                plaintext += letters[(letters.index(y) - keyValue) % 26]
    print(plaintext)


encrypt()
decrypt()
