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
        new_char = self.alphabet[(self.alphabet.index(char.lower()) + amount) % len(self.alphabet)]

        if self.case_strategy == 'maintain':
            new_char = new_char.upper() if char.isupper() else new_char.lower()

        return new_char

    def encrypt(self, plaintext: str) -> str:
        if self.key is None:
            raise AttributeError('key must be set before encryption')

        result: str = ""

        for char in plaintext:
            if char.lower() not in self.alphabet:
                if self.foreign_chars_strategy == 'keep': result += char
                continue

            result += self._shift(char, self.key)

        return result

    def decrypt(self, ciphertext: str) -> str:
        if self.key is None:
            raise AttributeError('key must be set before decryption')

        result: str = ""

        for char in ciphertext:
            if char.lower() not in self.alphabet:
                if self.foreign_chars_strategy == 'keep': result += char
                continue

            result += self._shift(char, -self.key)

        return result
