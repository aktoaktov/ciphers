from _base import BaseCipher, CaseStrategy, ForeignCharsStrategy
from alphabets import ENGLISH


class AtbashCipher(BaseCipher):
    alphabet: str
    case_strategy: CaseStrategy
    foreign_chars_strategy: ForeignCharsStrategy

    def __init__(self, alphabet: str = ENGLISH,
                 case_strategy: CaseStrategy = 'maintain',
                 foreign_chars_strategy: ForeignCharsStrategy = 'keep'):

        self.alphabet = alphabet
        self.case_strategy = case_strategy
        self.foreign_chars_strategy = foreign_chars_strategy

    def encrypt(self, plaintext: str) -> str:
        result: str = ""

        for char in plaintext:
            if char.lower() not in self.alphabet:
                if self.foreign_chars_strategy == 'keep': result += char
                continue

            new_char = self.alphabet[(-1 - self.alphabet.index(char.lower())) % len(self.alphabet)]

            if self.case_strategy == 'maintain':
                new_char = new_char.upper() if char.isupper() else new_char.lower()

            result += new_char

        return result

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)
