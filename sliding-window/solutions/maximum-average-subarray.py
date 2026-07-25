"""
Gabarito - Maximum Average Subarray I (LeetCode 643)

Ideia:
    Janela fixa de tamanho k. Somo os primeiros k, depois deslizo: a cada
    passo somo o novo elemento e tiro o que saiu da janela. Guardo a maior
    soma e divido por k no fim. O(n).
"""
from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    soma = sum(nums[:k])
    melhor = soma
    for i in range(k, len(nums)):
        soma += nums[i] - nums[i - k]
        melhor = max(melhor, soma)
    return melhor / k


# --- testes ---
if __name__ == "__main__":
    assert abs(find_max_average([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-6
    assert abs(find_max_average([5], 1) - 5.0) < 1e-6
    assert abs(find_max_average([0, 4, 0, 3, 2], 1) - 4.0) < 1e-6
    print("gabarito ok")
