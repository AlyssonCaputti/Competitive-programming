"""
Problema:   Top K Frequent Elements
Fonte:      LeetCode 347 - https://leetcode.com/problems/top-k-frequent-elements/
Nivel:      Medium
Tecnica:    hashmap, heap, bucket-sort

Enunciado:
    Dado um array de inteiros `nums` e um inteiro `k`, retorne os `k` elementos
    mais frequentes. A ordem da resposta nao importa.

Exemplo:
    nums = [1,1,1,2,2,3], k = 2  ->  [1, 2]
    nums = [1], k = 1            ->  [1]

Dica:
    Conte a frequencia num dicionario. Depois pegue os k maiores - da pra usar
    um heap, ou ordenar por frequencia, ou bucket sort por contagem (O(n)).
"""
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(top_k_frequent([1], 1)) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6], 2)) == [4, 5]
    print("todos os testes passaram")
