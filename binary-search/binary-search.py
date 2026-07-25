"""
Problema:   Binary Search
Fonte:      LeetCode 704 - https://leetcode.com/problems/binary-search/
Nivel:      Easy
Tecnica:    binary-search

Enunciado:
    Dado um array `nums` ordenado em ordem crescente e um `target`, retorne o
    indice de `target` em `nums`. Se nao existir, retorne -1. Precisa ser
    O(log n).

Exemplo:
    nums = [-1,0,3,5,9,12], target = 9   ->  4
    nums = [-1,0,3,5,9,12], target = 2   ->  -1

Dica:
    Mantenha dois limites (lo, hi). Olhe o meio: se for o alvo, achou; se for
    menor, jogue lo pra direita; se maior, hi pra esquerda. Cuidado com o
    criterio de parada pra nao entrar em loop.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([5], 5) == 0
    assert search([2, 5], 5) == 1
    assert search([], 1) == -1
    print("todos os testes passaram")
