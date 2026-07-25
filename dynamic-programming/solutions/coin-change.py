"""
Gabarito - Coin Change (LeetCode 322)

Ideia:
    DP bottom-up. dp[x] = menor numero de moedas pra formar x. Inicializo tudo
    com "infinito" (amount+1 serve) e dp[0]=0. Pra cada valor x, testo cada
    moeda que cabe: dp[x] = min(dp[x], dp[x-moeda]+1). O(amount * len(coins)).
"""
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    INF = amount + 1
    dp = [0] + [INF] * amount
    for x in range(1, amount + 1):
        for moeda in coins:
            if moeda <= x:
                dp[x] = min(dp[x], dp[x - moeda] + 1)
    return dp[amount] if dp[amount] != INF else -1


# --- testes ---
if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([2, 5, 10, 1], 27) == 4
    print("gabarito ok")
