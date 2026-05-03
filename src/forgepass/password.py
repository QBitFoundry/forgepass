import secrets
import string
from passlib.hash import sha256_crypt, sha512_crypt

def generate(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def hash(text: str, hash_type: str = "sha512"):
    hashed = "" # To make it secure it will return empty.
    if text:
        if hash_type == "sha256":
            hashed = sha256_crypt.hash(text)
        elif hash_type == "sha512":
            hashed = sha512_crypt.hash(text)
        else:
            options = ["sha256", "sha512"]
            formatted_options = ''.join(f'\\n - {option}' for option in options)
            raise ValueError(f"Invalid option. Choose one from: {formatted_options}")
            
    return hashed

class Generator:

    def __init__(self, length: int, hashed: bool, hash_type: str):
        self.length = length
        self.hashed = hashed
        self.hash_type = hash_type

    def get(self):
        password = generate(length=self.length)
        hashed = password

        if self.hashed:
            hashed = hash(text=password, hash_type=self.hash_type)
        
        return hashed


def main():
    password: str = generate()
    print(password)

if __name__ == "__main__":
    main()