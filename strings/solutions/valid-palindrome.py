"""
Gabarito - Valid Palindrome (LeetCode 125)

Ideia:
    Dois ponteiros nas pontas indo pro meio. Pulo o que nao e alfanumerico e
    comparo em minuscula. Se em algum ponto diferem, nao e palindromo.
    O(n) tempo, O(1) espaco (sem criar string nova).
"""


def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


# --- testes ---
if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    print("gabarito ok")
