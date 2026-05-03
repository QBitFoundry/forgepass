import secrets
import string

def password(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def main():
    pass_word: str = password(16)
    print(pass_word)

if __name__ == "__main__":
    main()