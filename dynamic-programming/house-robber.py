"""
Problema:   House Robber
Fonte:      LeetCode 198 - https://leetcode.com/problems/house-robber/
Nivel:      Medium
Tecnica:    dynamic-programming

Enunciado:
    Cada casa numa rua tem uma quantia `nums[i]`. Voce nao pode roubar duas
    casas adjacentes (dispara o alarme). Retorne a maior quantia que da pra
    roubar.

Exemplo:
    nums = [1,2,3,1]    ->  4   (casas 0 e 2: 1 + 3)
    nums = [2,7,9,3,1]  ->  12  (casas 0, 2 e 4: 2 + 9 + 1)

Dica:
    Pra cada casa, decida: roubo ela (e somo com o melhor de duas casas atras)
    ou pulo (fico com o melhor da casa anterior). dp[i] = max(dp[i-1],
    dp[i-2] + nums[i]). Da pra guardar so os dois ultimos valores.
"""
from typing import List


def rob(nums: List[int]) -> int:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([]) == 0
    assert rob([5]) == 5
    assert rob([2, 1, 1, 2]) == 4
    print("todos os testes passaram")
