"""
Gabarito - Longest Substring Without Repeating Characters (LeetCode 3)

Ideia:
    Janela deslizante com um dicionario {caractere: ultimo indice visto}.
    A borda esquerda (inicio) so anda pra frente quando reencontro um
    caractere que ja esta DENTRO da janela atual. O(n) tempo.
"""


def length_of_longest_substring(s: str) -> int:
    ultimo = {}       # caractere -> ultimo indice onde apareceu
    inicio = 0
    melhor = 0
    for i, c in enumerate(s):
        if c in ultimo and ultimo[c] >= inicio:
            inicio = ultimo[c] + 1
        ultimo[c] = i
        melhor = max(melhor, i - inicio + 1)
    return melhor


# --- testes ---
if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("dvdf") == 3
    print("gabarito ok")
