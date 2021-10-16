from rsa import rsa as rsa_enc

print("RSA_ENCRYPTION Demo")

def main():
    rsa = rsa_enc(2, 19)
    rsa.generateKeys()

    message = input("\nEnter a alphanumerical string: ")
    while message != '!':
        print("\nMessage: {}".format(message))

        enc = rsa.encrypt(message)
        print("     Encrypted message: {}".format(enc))

        dec = rsa.decrypt(enc)
        print("     Decrypted message: {}".format(dec))
        message = input("\nEnter a alphanumerical string: ")

    print("\nExit RSA encrypter\n")

if __name__ == '__main__':
    main()
