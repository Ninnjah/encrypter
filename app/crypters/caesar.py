"""Caesar encrypter/decrypter module"""
import string


def encrypt(text: str, step: int, alphabeth: str = string.ascii_lowercase) -> str:
    """Encrypt text with Caesar crypt
        text: str, text for encrypting
        step: int, encrypting step
        alphabeth: str = string.ascii_lowercase, encrypting alphabeth

        returns: str, encrypted text
    """
    encrypted_text = ""

    for letter in text:
        try:
            letter_index = alphabeth.index(letter)

        except ValueError:
            encrypted_text += letter
            continue

        else:
            encrypted_text += alphabeth[(letter_index + step) % len(alphabeth)]

    return encrypted_text


if __name__ == "__main__":
    print(encrypt(input(), 5))

