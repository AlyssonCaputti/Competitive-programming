# Caderno de algoritmos

Estudo de algoritmos e estruturas de dados, organizado por técnica. Cada
problema tem o enunciado, testes pra validar a resposta e um gabarito pra
conferir depois de tentar.

## Estrutura

```
<categoria>/
    <problema>.py            enunciado + testes (é aqui que você resolve)
    solutions/
        <problema>.py        gabarito comentado (só olhe depois de tentar)
PROBLEMS.md                  lista de todos os problemas, com o que já resolvi
templates/                   esqueletos pra começar um problema novo
```

A extensão do arquivo já diz a linguagem (`.py`, `.cpp`, `.sql`), então não
separo em subpastas por linguagem. A pasta de uma categoria só existe quando
tem pelo menos um problema dela.

## Como resolver

Cada arquivo de atividade tem o enunciado no topo, uma função vazia pra você
implementar e os testes no fim. O fluxo é:

```bash
# 1. abra o arquivo e implemente a função
#    ex: arrays/two-sum.py

# 2. rode pra ver se passou
python arrays/two-sum.py

# se passar, aparece "todos os testes passaram".
# se travar, o gabarito está em arrays/solutions/two-sum.py
```

Os testes usam `assert`. Se um falhar, o Python aponta qual caso quebrou.

## Categorias

`arrays` · `strings` · `hashmaps` · `two-pointers` · `sliding-window` ·
`binary-search` · `dynamic-programming` · `graphs` · `stacks-and-queues` ·
`sorting`

A lista completa dos problemas está em [`PROBLEMS.md`](PROBLEMS.md).

## Templates

- [`templates/template.py`](templates/template.py): esqueleto Python
- [`templates/template.cpp`](templates/template.cpp): esqueleto C++ com fast I/O
- [`templates/explanation.md`](templates/explanation.md): pra explicar um problema mais a fundo

## Licença

[MIT](LICENSE). Use à vontade.
