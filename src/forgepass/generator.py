import secrets
import string

def main():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(16))
    print(password)

if __name__ == "__main__":
    main()