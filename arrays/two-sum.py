"""
Problema:   Two Sum
Fonte:      LeetCode 1 - https://leetcode.com/problems/two-sum/
Nivel:      Easy
Tecnica:    arrays, hashmap

Enunciado:
    Dado um array de inteiros `nums` e um inteiro `target`, retorne os indices
    dos dois numeros que somam `target`. Cada entrada tem exatamente uma
    solucao, e voce nao pode usar o mesmo elemento duas vezes.

Exemplo:
    nums = [2, 7, 11, 15], target = 9  ->  [0, 1]   (2 + 7 = 9)
    nums = [3, 2, 4], target = 6       ->  [1, 2]   (2 + 4 = 6)

Dica:
    Da pra fazer O(n^2) testando todos os pares. Consegue O(n) guardando o que
    ja viu num dicionario?
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]
    print("todos os testes passaram")
