"""
Problema:   Coin Change
Fonte:      LeetCode 322 - https://leetcode.com/problems/coin-change/
Nivel:      Medium
Tecnica:    dynamic-programming

Enunciado:
    Dadas moedas de valores `coins` (quantidade ilimitada de cada) e um valor
    `amount`, retorne o menor numero de moedas que somam exatamente `amount`.
    Se nao for possivel, retorne -1.

Exemplo:
    coins = [1,2,5], amount = 11  ->  3   (5 + 5 + 1)
    coins = [2], amount = 3       ->  -1
    coins = [1], amount = 0       ->  0

Dica:
    dp[x] = menor numero de moedas pra formar x. Comece dp[0] = 0 e o resto
    "infinito". Pra cada valor x, tente cada moeda: dp[x] = min(dp[x],
    dp[x - moeda] + 1).
"""
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([2, 5, 10, 1], 27) == 4
    print("todos os testes passaram")
