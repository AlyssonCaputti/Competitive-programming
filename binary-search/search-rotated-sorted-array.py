"""
Problema:   Search in Rotated Sorted Array
Fonte:      LeetCode 33 - https://leetcode.com/problems/search-in-rotated-sorted-array/
Nivel:      Medium
Tecnica:    binary-search

Enunciado:
    Um array ordenado foi rotacionado em algum pivo desconhecido (ex:
    [0,1,2,4,5,6,7] pode virar [4,5,6,7,0,1,2]). Dado o array rotacionado
    `nums` (valores distintos) e um `target`, retorne o indice do alvo ou -1.
    Precisa ser O(log n).

Exemplo:
    nums = [4,5,6,7,0,1,2], target = 0   ->  4
    nums = [4,5,6,7,0,1,2], target = 3   ->  -1
    nums = [1], target = 0               ->  -1

Dica:
    Busca binaria adaptada: a cada meio, um dos lados (esquerda ou direita)
    esta ordenado. Descubra qual e veja se o alvo cai no intervalo ordenado;
    senao, va pro outro lado.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([5, 1, 3], 5) == 0
    assert search([4, 5, 6, 7, 0, 1, 2], 6) == 2
    print("todos os testes passaram")
