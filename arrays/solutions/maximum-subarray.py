"""
Gabarito - Maximum Subarray (LeetCode 53) - Kadane

Ideia:
    Pra cada elemento, a melhor soma que termina nele e: ou o proprio elemento
    (comeca subarray novo), ou ele somado com a melhor soma que terminava no
    anterior. Guardo o melhor global visto. O(n) tempo, O(1) espaco.
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    melhor_aqui = melhor_global = nums[0]
    for num in nums[1:]:
        melhor_aqui = max(num, melhor_aqui + num)
        melhor_global = max(melhor_global, melhor_aqui)
    return melhor_global


# --- testes ---
if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1, -2, -3]) == -1
    print("gabarito ok")
