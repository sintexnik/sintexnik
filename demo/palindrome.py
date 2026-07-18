"""Palindrome check utility.

Provides is_palindrome(s: str) -> bool, which determines whether the
given string is a palindrome, ignoring letter case and whitespace
characters. No third-party dependencies are used.
"""


def is_palindrome(s: str) -> bool:
    """Return True if `s` is a palindrome, ignoring case and whitespace.

    Whitespace characters (spaces, tabs, newlines, etc.) are removed
    before comparison, and the comparison is case-insensitive.

    Examples:
        >>> is_palindrome("")
        True
        >>> is_palindrome("   ")
        True
        >>> is_palindrome("a")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello world")
        False
    """
    normalized = "".join(ch.lower() for ch in s if not ch.isspace())
    return normalized == normalized[::-1]
