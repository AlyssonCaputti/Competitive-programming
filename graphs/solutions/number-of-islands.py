"""
Gabarito - Number of Islands (LeetCode 200)

Ideia:
    Varro a grade. Ao achar terra ('1') nao visitada, incremento o contador e
    "afundo" a ilha inteira com DFS, marcando cada terra conectada como '0'
    pra nao contar de novo. O(linhas * colunas).
"""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    linhas, colunas = len(grid), len(grid[0])

    def afunda(r, c):
        if r < 0 or r >= linhas or c < 0 or c >= colunas or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        afunda(r + 1, c)
        afunda(r - 1, c)
        afunda(r, c + 1)
        afunda(r, c - 1)

    ilhas = 0
    for r in range(linhas):
        for c in range(colunas):
            if grid[r][c] == "1":
                ilhas += 1
                afunda(r, c)
    return ilhas


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
    print("gabarito ok")
