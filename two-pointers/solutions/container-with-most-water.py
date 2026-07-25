"""
Gabarito - Container With Most Water (LeetCode 11)

Ideia:
    Dois ponteiros nas pontas. A area e limitada pela linha mais baixa, entao
    mover a mais baixa pra dentro e a unica jogada que pode aumentar a area
    (mover a mais alta so diminui a largura sem ganhar altura). O(n).
"""
from typing import List


def max_area(height: List[int]) -> int:
    i, j = 0, len(height) - 1
    melhor = 0
    while i < j:
        altura = min(height[i], height[j])
        melhor = max(melhor, altura * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return melhor


# --- testes ---
if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("gabarito ok")
