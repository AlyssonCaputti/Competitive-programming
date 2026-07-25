"""
Problema:   Merge Intervals
Fonte:      LeetCode 56 - https://leetcode.com/problems/merge-intervals/
Nivel:      Medium
Tecnica:    sorting, intervalos

Enunciado:
    Dada uma lista de intervalos `[inicio, fim]`, junte todos os que se
    sobrepoem e retorne a lista de intervalos resultante.

Exemplo:
    [[1,3],[2,6],[8,10],[15,18]]  ->  [[1,6],[8,10],[15,18]]
    [[1,4],[4,5]]                 ->  [[1,5]]

Dica:
    Ordene por inicio. Percorra: se o intervalo atual comeca antes (ou no)
    fim do ultimo do resultado, eles se sobrepoem - estenda o fim. Senao,
    adicione como um novo.
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[1, 4]]) == [[1, 4]]
    print("todos os testes passaram")
