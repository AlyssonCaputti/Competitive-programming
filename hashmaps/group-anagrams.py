"""
Problema:   Group Anagrams
Fonte:      LeetCode 49 - https://leetcode.com/problems/group-anagrams/
Nivel:      Medium
Tecnica:    hashmap, strings

Enunciado:
    Dada uma lista de strings, agrupe os anagramas. Anagramas sao palavras
    formadas pelas mesmas letras em ordem diferente. A ordem dos grupos e dos
    itens dentro do grupo nao importa.

Exemplo:
    ["eat","tea","tan","ate","nat","bat"]
        ->  [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Dica:
    Duas palavras sao anagramas se as letras ordenadas sao iguais. Use isso
    (a string ordenada) como chave de um dicionario.
"""
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    # implemente aqui
    pass


# --- testes ---
def _normaliza(grupos):
    # ordena pra comparar sem depender da ordem
    return sorted(sorted(g) for g in grupos)


if __name__ == "__main__":
    r1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert _normaliza(r1) == _normaliza([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    assert _normaliza(group_anagrams([""])) == [[""]]
    assert _normaliza(group_anagrams(["a"])) == [["a"]]
    print("todos os testes passaram")
