import bloat_cipher


def main():
    cipher = bloat_cipher.BloatCipher(".")
    cipher.encrypt("../data/encrypt_test.txt")
    cipher.decrypt("../data/decrypt_test.bloat")


if __name__ == '__main__':
    main()
