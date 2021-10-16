from rsa import rsa as rsa_enc

def main():
    print("RSA_ENCRYPTION Demo")

    rsa = rsa_enc(2, 19)
    rsa.generateKeys()
    message = 1
    while message > 0:
        message = int(input("Please enter a number (0 < x < 14): "))
        print("Message: {}".format(message))

        enc = rsa.encrypt(message)
        print("Encrypted message: {}".format(enc))

        dec = rsa.decrypt(enc)
        print("Decrypted message: {}".format(dec))

if __name__ == '__main__':
    main()
