"""
Gabarito - Top K Frequent Elements (LeetCode 347)

Ideia:
    Conto frequencia com Counter. Depois bucket sort: indice = frequencia,
    valor = lista de numeros com aquela frequencia. Varro dos buckets mais
    altos pros mais baixos ate juntar k. O(n) - melhor que ordenar.
"""
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    contagem = Counter(nums)
    # buckets[f] = numeros que aparecem f vezes
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in contagem.items():
        buckets[freq].append(num)

    resultado = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            resultado.append(num)
            if len(resultado) == k:
                return resultado
    return resultado


# --- testes ---
if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(top_k_frequent([1], 1)) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6], 2)) == [4, 5]
    print("gabarito ok")
