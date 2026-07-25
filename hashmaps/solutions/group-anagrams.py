"""
Gabarito - Group Anagrams (LeetCode 49)

Ideia:
    Anagramas tem as mesmas letras -> a string ordenada e igual. Uso a string
    ordenada como chave de um dicionario que agrupa as palavras.
    O(n * k log k), com k = tamanho medio das palavras.
"""
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    grupos = defaultdict(list)
    for palavra in strs:
        chave = "".join(sorted(palavra))
        grupos[chave].append(palavra)
    return list(grupos.values())


# --- testes ---
def _normaliza(grupos):
    return sorted(sorted(g) for g in grupos)


if __name__ == "__main__":
    r1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert _normaliza(r1) == _normaliza([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert _normaliza(group_anagrams([""])) == [[""]]
    assert _normaliza(group_anagrams(["a"])) == [["a"]]
    print("gabarito ok")
