"""
Problema:   Valid Parentheses
Fonte:      LeetCode 20 - https://leetcode.com/problems/valid-parentheses/
Nivel:      Easy
Tecnica:    stack

Enunciado:
    Dada uma string `s` so com os caracteres '(', ')', '{', '}', '[' e ']',
    determine se ela esta balanceada: todo par abre/fecha do tipo certo e na
    ordem certa.

Exemplo:
    "()"      ->  True
    "()[]{}"  ->  True
    "(]"      ->  False
    "([)]"    ->  False
    "{[]}"    ->  True

Dica:
    Pilha: empilhe os que abrem. Quando vier um que fecha, o topo da pilha tem
    que ser o par correspondente. No fim, a pilha tem que estar vazia.
"""


def is_valid(s: str) -> bool:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("(") is False
    assert is_valid("") is True
    print("todos os testes passaram")
