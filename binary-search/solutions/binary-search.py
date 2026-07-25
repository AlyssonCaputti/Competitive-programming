"""
Gabarito - Binary Search (LeetCode 704)

Ideia:
    Limites lo e hi inclusivos. Olho o meio: se e o alvo, retorno; se o meio e
    menor, o alvo esta a direita (lo = mid+1); senao a esquerda (hi = mid-1).
    Paro quando lo passa hi. O(log n).
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# --- testes ---
if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([5], 5) == 0
    assert search([2, 5], 5) == 1
    assert search([], 1) == -1
    print("gabarito ok")
