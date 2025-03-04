from substitutions.caesar import CaesarCipher

caesar = CaesarCipher()

for key in range(26):
    caesar.set_key(key)
    plaintext = "Hello! I am caesar cipher."
    encrypted = caesar.encrypt(plaintext)
    print(key, encrypted, caesar.decrypt(encrypted) == plaintext)
