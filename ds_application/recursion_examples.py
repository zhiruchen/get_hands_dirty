# encoding: utf-8


def reverse_str(m_str):
    if len(m_str) == 1:
        return m_str
    else:
        return m_str[-1] + reverse_str(m_str[:-1])


def palindrome_check(m_str):
    return m_str == reverse_str(m_str)


def test_reverse_str():
    assert reverse_str("abc") == "cba"
    assert reverse_str("roor") == "roor"
    assert reverse_str("Python") == "nohtyP"


def test_palindrome_check():
    assert palindrome_check("abc") is False
    assert palindrome_check("roor") is True
    assert palindrome_check("radar") is True
