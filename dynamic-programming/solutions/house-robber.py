"""
Gabarito - House Robber (LeetCode 198)

Ideia:
    DP guardando so dois valores: o melhor considerando ate a casa anterior
    (prev) e ate duas casas atras (prev2). Pra cada casa: roubo (prev2 + atual)
    ou nao roubo (prev), fico com o maior. O(n) tempo, O(1) espaco.
"""
from typing import List


def rob(nums: List[int]) -> int:
    prev2, prev = 0, 0
    for valor in nums:
        prev2, prev = prev, max(prev, prev2 + valor)
    return prev


# --- testes ---
if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([]) == 0
    assert rob([5]) == 5
    assert rob([2, 1, 1, 2]) == 4
    print("gabarito ok")
