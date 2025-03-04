from _base import BaseCipher, CaseStrategy, ForeignCharsStrategy
from alphabets import ENGLISH


class CaesarCipher(BaseCipher):
    alphabet: str
    case_strategy: CaseStrategy
    foreign_chars_strategy: ForeignCharsStrategy

    key: int | None

    def __init__(self, alphabet: str = ENGLISH,
                 case_strategy: CaseStrategy = 'maintain',
                 foreign_chars_strategy: ForeignCharsStrategy = 'keep'):

        self.alphabet = alphabet
        self.case_strategy = case_strategy
        self.foreign_chars_strategy = foreign_chars_strategy

        self.key = None

    def set_key(self, key: int | None):
        self.key = key

    def _shift(self, char: str, amount: int) -> str:
        encrypted_char = self.alphabet[(self.alphabet.index(char.lower()) + amount) % len(self.alphabet)]

        if self.case_strategy == 'maintain':
            encrypted_char = encrypted_char.upper() if char.isupper() else encrypted_char.lower()

        return encrypted_char

    def encrypt(self, plaintext: str) -> str:
        if self.key is None:
            raise ValueError('key must be set before encryption')

        result = ""

        for char in plaintext:
            if char.lower() not in self.alphabet:
                if self.foreign_chars_strategy == 'keep': result += char
                continue

            result += self._shift(char, self.key)

        return result

    def decrypt(self, ciphertext: str) -> str:
        if self.key is None:
            raise ValueError('key must be set before decryption')

        result = ""

        for char in ciphertext:
            if char.lower() not in self.alphabet:
                if self.foreign_chars_strategy == 'keep': result += char
                continue

            result += self._shift(char, -self.key)

        return result
