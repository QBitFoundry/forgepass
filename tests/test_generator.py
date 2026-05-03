import pytest
from forgepass.password import generate, hash, Generator

def test_default_length():
    """Check if the default password is 16 characters."""
    password = generate()
    assert len(password) == 16

def test_custom_length():
    """Check if the custom length argument works."""
    length = 32
    password = generate(length=length)
    assert len(password) == length

def test_is_string():
    """Ensure the output is actually a string and not empty."""
    password = generate()
    assert isinstance(password, str)
    assert len(password) > 0

def test_randomness():
    """Check that two generated passwords are not the same (basic check)."""
    pw1 = generate()
    pw2 = generate()
    assert pw1 != pw2

def test_default_hashing():
    """Check that the password can be hashed."""
    password = generate()
    hashed1 = hash(text=password)
    hashed2 = hash(text=password)
    assert password != hashed1 and password != hashed2
    assert hashed1 != hashed2

def test_hash_with_invalid_type():
    """Check if it return empty string when text parameter is not provides"""
    with pytest.raises(ValueError):
        hashed = hash("Some Text", "abc")


def test_generator():
    """Check if the Generator class module works as expected"""
    generator = Generator(
        length=32,
        hashed=True,
        hash_type="sha256"
    )

    hashed_password = generator.get()
    assert hashed_password