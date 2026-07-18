"""Tests for demo.palindrome.is_palindrome."""

from palindrome import is_palindrome


def test_empty_string_is_palindrome():
    assert is_palindrome("") is True


def test_whitespace_only_string_is_palindrome():
    assert is_palindrome("   ") is True


def test_single_character_is_palindrome():
    assert is_palindrome("a") is True


def test_single_character_uppercase_is_palindrome():
    assert is_palindrome("Z") is True


def test_classic_phrase_ignoring_case_and_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True


def test_non_palindrome_phrase():
    assert is_palindrome("hello world") is False


def test_simple_palindrome_word():
    assert is_palindrome("racecar") is True


def test_mixed_case_palindrome_word():
    assert is_palindrome("RaceCar") is True


def test_palindrome_with_tabs_and_newlines():
    assert is_palindrome("no\ton\n") is True


def test_non_palindrome_single_word():
    assert is_palindrome("python") is False
