
import string

class Base62Encoder:
    ALPHABET = string.digits + string.ascii_letters
    BASE = len(ALPHABET)

    @classmethod
    def encode(cls, number: int) -> str:
        if number < 0:
            raise ValueError("Number must be non-negative")
        if number == 0:
            return cls.ALPHABET[0]
        result = []
        while number > 0:
            number, remainder = divmod(number, cls.BASE)
            result.append(cls.ALPHABET[remainder])
        return ''.join(reversed(result))
