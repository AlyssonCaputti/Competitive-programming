"""
Gabarito - Two Sum (LeetCode 1)

Ideia:
    Um passo pelo array guardando num dicionario {valor: indice} o que ja vi.
    Pra cada numero, o complemento que falta e (target - num). Se o
    complemento ja esta no dicionario, achei o par. O(n) tempo, O(n) espaco.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    visto = {}  # valor -> indice
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in visto:
            return [visto[complemento], i]
        visto[num] = i
    return []  # nao deveria chegar aqui (o enunciado garante 1 solucao)


# --- testes (mesmos do exercicio) ---
if __name__ == "__main__":
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]
    print("gabarito ok")
