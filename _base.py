from abc import ABC
from typing import Literal

type CaseStrategy = Literal['maintain', 'ignore']
type ForeignCharsStrategy = Literal['keep', 'ignore']


class BaseCipher(ABC):
    def encrypt(self, plaintext: str) -> str:
        raise NotImplementedError

    def decrypt(self, ciphertext: str) -> str:
        raise NotImplementedError
