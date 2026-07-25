"""
Problema:   Maximum Average Subarray I
Fonte:      LeetCode 643 - https://leetcode.com/problems/maximum-average-subarray-i/
Nivel:      Easy
Tecnica:    sliding-window

Enunciado:
    Dado um array `nums` e um inteiro `k`, encontre a maior media possivel de
    um subarray contiguo de tamanho exatamente `k`. Retorne essa media (float).

Exemplo:
    nums = [1,12,-5,-6,50,3], k = 4  ->  12.75   (subarray [12,-5,-6,50])
    nums = [5], k = 1                ->  5.0

Dica:
    Janela fixa de tamanho k: some os primeiros k, depois deslize somando o
    novo e subtraindo o que saiu. Nao recalcule a soma toda vez.
"""
from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert abs(find_max_average([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-6
    assert abs(find_max_average([5], 1) - 5.0) < 1e-6
    assert abs(find_max_average([0, 4, 0, 3, 2], 1) - 4.0) < 1e-6
    print("todos os testes passaram")
