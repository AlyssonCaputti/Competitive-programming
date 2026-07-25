"""
Gabarito - Search in Rotated Sorted Array (LeetCode 33)

Ideia:
    Busca binaria. A cada meio, um dos lados esta ordenado. Descubro qual
    (comparando nums[lo] com nums[mid]) e vejo se o alvo cai no intervalo
    ordenado desse lado; se cai, vou pra la, senao pro outro lado. O(log n).
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        # lado esquerdo esta ordenado?
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # entao o lado direito esta ordenado
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# --- testes ---
if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([5, 1, 3], 5) == 0
    assert search([4, 5, 6, 7, 0, 1, 2], 6) == 2
    print("gabarito ok")
