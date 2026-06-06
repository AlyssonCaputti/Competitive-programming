# Programação Competitiva

Repositório de estudo contínuo — soluções organizadas por técnica, com foco em entender o problema antes de resolver.

Cada solução tem cabeçalho com abordagem, complexidade e raciocínio. Não é só código — é o processo de pensar.

---

## Por que esse repositório existe

Estudo algoritmos com consistência porque acredito que pensar bem sobre complexidade muda a qualidade de qualquer código que você escreve — seja numa competição ou num pipeline em produção.

O objetivo não é volume. É entender de verdade cada técnica antes de passar pra próxima.

---

## Estrutura

```
<categoria>/
    ├── exercises.md     # lista de problemas (Fácil / Médio / Difícil)
    ├── python/          # soluções em Python
    │     └── <problema>.py
    └── cpp/             # soluções em C++
          └── <problema>.cpp
```

Para SQL, as soluções ficam direto dentro da pasta `sql/` como arquivos `.sql`.

---

## Categorias

`arrays` · `strings` · `hashmaps` · `linked-lists` · `stacks-and-queues` · `trees` · `graphs` · `heaps` · `dynamic-programming` · `greedy` · `backtracking` · `binary-search` · `two-pointers` · `sliding-window` · `bit-manipulation` · `math` · `sorting` · `recursion` · `sql`

Quando um problema se encaixa em mais de uma categoria, o critério é a **técnica principal** usada pra resolver.

---

## Foco atual

Estudando com prioridade:

- Two Pointers e Sliding Window
- Binary Search (variações e aplicações)
- Dynamic Programming (bottom-up)
- Grafos (BFS, DFS, caminhos mínimos)

---

## Como adicionar uma solução

1. Escolha a categoria certa
2. Abra o `exercises.md` da categoria e localize o problema (ou adicione)
3. Crie o arquivo usando o template da linguagem:
   - Python: `<categoria>/python/<nome-do-problema>.py`
   - C++: `<categoria>/cpp/<nome-do-problema>.cpp`
4. Preencha o cabeçalho antes de commitar — fonte, dificuldade, abordagem, complexidade

---

## Convenções

- Nomes de arquivos e pastas em **kebab-case** minúsculo (`two-sum.py`, não `TwoSum.py`)
- Um arquivo por problema — o cabeçalho é a explicação
- Nome canônico do problema, sem número ou prefixo de plataforma
- Commit: `<categoria>: <verbo> <nome-do-problema>` — ex: `arrays: add two-sum`, `dp: refactor lis to O(n log n)`

---

## Templates

- [`templates/template.py`](templates/template.py) — esqueleto Python com cabeçalho de docstring
- [`templates/template.cpp`](templates/template.cpp) — esqueleto C++ com macros e fast I/O
- [`templates/explanation.md`](templates/explanation.md) — template de write-up longo, quando o cabeçalho não é suficiente

---

Licença [MIT](LICENSE).
