from rsa import rsa as rsa_enc

def main():
    print("RSA_ENCRYPTION Demo")

    rsa = rsa_enc(2, 19)
    rsa.generateKeys()
    message = ''
    while message != '!':
        message = input("Enter a alphanumerical string: ")
        print("Message: {}".format(message))

        enc = rsa.encrypt(message)
        print("Encrypted message: {}".format(enc))

        dec = rsa.decrypt(enc)
        print("Decrypted message: {}".format(dec))

if __name__ == '__main__':
    main()
