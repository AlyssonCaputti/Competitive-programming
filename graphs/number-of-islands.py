"""
Problema:   Number of Islands
Fonte:      LeetCode 200 - https://leetcode.com/problems/number-of-islands/
Nivel:      Medium
Tecnica:    graphs, DFS/BFS, matriz

Enunciado:
    Dada uma grade 2D de '1' (terra) e '0' (agua), conte quantas ilhas existem.
    Uma ilha e um grupo de terras conectadas na horizontal ou vertical (nao na
    diagonal). A borda da grade e toda cercada por agua.

Exemplo:
    grid = [
        ["1","1","0","0"],
        ["1","1","0","0"],
        ["0","0","1","0"],
        ["0","0","0","1"],
    ]                         ->  3

Dica:
    Percorra a grade. Ao achar um '1' ainda nao visitado, e uma ilha nova -
    faca DFS/BFS marcando toda a terra conectada como visitada (ex: trocando
    por '0') pra nao contar de novo.
"""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    g1 = [
        ["1", "1", "0", "0"],
        ["1", "1", "0", "0"],
        ["0", "0", "1", "0"],
        ["0", "0", "0", "1"],
    ]
    assert num_islands(g1) == 3

    g2 = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"],
    ]
    assert num_islands(g2) == 1

    assert num_islands([["0"]]) == 0
    assert num_islands([["1"]]) == 1
    print("todos os testes passaram")
