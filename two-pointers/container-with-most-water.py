"""
Problema:   Container With Most Water
Fonte:      LeetCode 11 - https://leetcode.com/problems/container-with-most-water/
Nivel:      Medium
Tecnica:    two-pointers

Enunciado:
    Dado um array `height` onde cada valor e a altura de uma linha vertical na
    posicao i, escolha duas linhas que, junto com o eixo x, formem um
    recipiente que segure a maior quantidade de agua. Retorne essa area maxima.
    A area e limitada pela linha mais baixa: min(h[i], h[j]) * (j - i).

Exemplo:
    height = [1,8,6,2,5,4,8,3,7]  ->  49
    height = [1,1]               ->  1

Dica:
    Dois ponteiros nas pontas. A cada passo, mova o ponteiro da linha MAIS
    BAIXA pra dentro (mover a mais alta nunca melhora).
"""
from typing import List


def max_area(height: List[int]) -> int:
    # implemente aqui
    pass


# --- testes ---
if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("todos os testes passaram")
