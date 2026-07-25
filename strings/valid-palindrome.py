"""
Problema:   Valid Palindrome
Fonte:      LeetCode 125 - https://leetcode.com/problems/valid-palindrome/
Nivel:      Easy
Tecnica:    strings, two-pointers

Enunciado:
    Uma frase e um palindromo se, lendo so os caracteres alfanumericos e
    ignorando maiuscula/minuscula, ela fica igual de tras pra frente.
    Retorne True se `s` for palindromo, False caso contrario.

Exemplo:
    "A man, a plan, a canal: Panama"  ->  True   ("amanaplanacanalpanama")
    "race a car"                      ->  False
    " "                               ->  True    (string vazia apos limpar)

Dica:
    Limpe a string (so letras/numeros, tudo minusculo) e compare com o reverso.
    Ou use dois ponteiros vindo das pontas pro meio.
"""


def is_palindrome(s: str) -> bool:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    print("todos os testes passaram")
