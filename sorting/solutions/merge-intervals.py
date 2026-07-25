"""
Gabarito - Merge Intervals (LeetCode 56)

Ideia:
    Ordeno por inicio. Percorro: se o intervalo atual comeca antes ou igual ao
    fim do ultimo do resultado, eles se sobrepoem -> estendo o fim do ultimo.
    Senao, adiciono como novo. O(n log n) por causa da ordenacao.
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    resultado = [intervals[0][:]]
    for inicio, fim in intervals[1:]:
        if inicio <= resultado[-1][1]:
            resultado[-1][1] = max(resultado[-1][1], fim)
        else:
            resultado.append([inicio, fim])
    return resultado


# --- testes ---
if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[1, 4]]) == [[1, 4]]
    print("gabarito ok")
