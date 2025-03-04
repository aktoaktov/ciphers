from math import gcd

from _base import BaseCipher, CaseStrategy, ForeignCharsStrategy
from alphabets import ENGLISH


class AffineCipher(BaseCipher):
    alphabet: str
    case_strategy: CaseStrategy
    foreign_chars_strategy: ForeignCharsStrategy

    a: int | None
    b: int | None

    def __init__(self, alphabet: str = ENGLISH,
                 case_strategy: CaseStrategy = 'maintain',
                 foreign_chars_strategy: ForeignCharsStrategy = 'keep'):

        self.alphabet = alphabet
        self.case_strategy = case_strategy
        self.foreign_chars_strategy = foreign_chars_strategy

        self.a = None
        self.b = None

    def set_keys(self, a: int, b: int):
        if gcd(a, len(self.alphabet)) != 1:
            raise ValueError(f"a must have inverse by modulo {len(self.alphabet)}")

        self.a = a
        self.b = b

    def encrypt(self, plaintext: str) -> str:
        if self.a is None or self.b is None:
            raise ValueError(f"a and b must be set before encryption")

        result = ""

        for char in plaintext:
            if char.lower() not in self.alphabet:
                if self.foreign_chars_strategy == 'keep': result += char
                continue

            encrypted_char = self.alphabet[
                (self.a * self.alphabet.index(char.lower()) + self.b)
                % len(self.alphabet)]

            if self.case_strategy == 'maintain':
                encrypted_char = encrypted_char.upper() if char.isupper() else encrypted_char.lower()

            result += encrypted_char

        return result

    def decrypt(self, ciphertext: str) -> str:
        if self.a is None or self.b is None:
            raise ValueError(f"a and b must be set before decryption")

        result = ""

        for char in ciphertext:
            if char.lower() not in self.alphabet:
                if self.foreign_chars_strategy == 'keep': result += char
                continue

            encrypted_char = self.alphabet[
                (pow(self.a, -1, len(self.alphabet)) * (self.alphabet.index(char.lower()) - self.b))
                % len(self.alphabet)]

            if self.case_strategy == 'maintain':
                encrypted_char = encrypted_char.upper() if char.isupper() else encrypted_char.lower()

            result += encrypted_char

        return result
