"""
Problema:   Longest Substring Without Repeating Characters
Fonte:      LeetCode 3 - https://leetcode.com/problems/longest-substring-without-repeating-characters/
Nivel:      Medium
Tecnica:    strings, sliding-window, hashmap

Enunciado:
    Dada uma string `s`, encontre o comprimento da maior substring sem
    caracteres repetidos.

Exemplo:
    "abcabcbb"  ->  3   ("abc")
    "bbbbb"     ->  1   ("b")
    "pwwkew"    ->  3   ("wke")

Dica:
    Janela deslizante: va expandindo a direita e, quando repetir um caractere,
    encolha a esquerda ate nao repetir mais. Guarde a ultima posicao de cada
    caractere num dicionario.
"""


def length_of_longest_substring(s: str) -> int:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("dvdf") == 3
    print("todos os testes passaram")
