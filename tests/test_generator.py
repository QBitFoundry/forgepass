import pytest
from forgepass.generator import password

def test_default_length():
    """Check if the default password is 16 characters."""
    pass_word = password()
    assert len(pass_word) == 16

def test_custom_length():
    """Check if the custom length argument works."""
    length = 32
    pass_word = password(length=length)
    assert len(pass_word) == length

def test_is_string():
    """Ensure the output is actually a string and not empty."""
    pass_word = password()
    assert isinstance(pass_word, str)
    assert len(pass_word) > 0

def test_randomness():
    """Check that two generated passwords are not the same (basic check)."""
    pw1 = password()
    pw2 = password()
    assert pw1 != pw2
