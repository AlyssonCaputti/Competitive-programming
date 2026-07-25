"""
Problema:   Maximum Subarray
Fonte:      LeetCode 53 - https://leetcode.com/problems/maximum-subarray/
Nivel:      Medium
Tecnica:    arrays, dynamic-programming (Kadane)

Enunciado:
    Dado um array de inteiros `nums`, encontre o subarray contiguo (com pelo
    menos um elemento) que tem a maior soma, e retorne essa soma.

Exemplo:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  ->  6   (subarray [4, -1, 2, 1])
    nums = [1]                              ->  1
    nums = [5, 4, -1, 7, 8]                 ->  23

Dica:
    Algoritmo de Kadane: pra cada posicao, decida se comeca um subarray novo
    ali ou continua o anterior. Va guardando o melhor visto ate agora.
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1, -2, -3]) == -1
    print("todos os testes passaram")
