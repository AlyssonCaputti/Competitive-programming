"""
Gabarito - Valid Parentheses (LeetCode 20)

Ideia:
    Pilha. Ao ver um que abre, empilho. Ao ver um que fecha, o topo tem que
    ser o par de abertura correspondente (uso um mapa fecha->abre). Se nao
    bater, ou a pilha estiver vazia, invalido. No fim a pilha tem que zerar.
"""


def is_valid(s: str) -> bool:
    par = {")": "(", "]": "[", "}": "{"}
    pilha = []
    for c in s:
        if c in par:  # e um caractere de fechamento
            if not pilha or pilha.pop() != par[c]:
                return False
        else:
            pilha.append(c)
    return not pilha


# --- testes ---
if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("(") is False
    assert is_valid("") is True
    print("gabarito ok")
