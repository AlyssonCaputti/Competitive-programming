# Competitive Programming

My solutions to algorithm and data-structure problems, grouped by topic. Each category folder has a curated list of practice problems and language-specific solution folders.

## Structure

```
<category>/
    ├── exercises.md          # curated problems (Easy / Medium / Hard)
    ├── python/               # solutions in Python
    │     └── <problem>.py
    └── cpp/                  # solutions in C++
          └── <problem>.cpp
```

Example:

```
arrays/
    ├── exercises.md
    ├── python/
    │     └── two-sum.py
    └── cpp/
          └── two-sum.cpp
```

For SQL there is no language split — solutions live directly inside `sql/` as `.sql` files.

## Categories

`arrays` · `strings` · `hashmaps` · `linked-lists` · `stacks-and-queues` · `trees` · `graphs` · `heaps` · `dynamic-programming` · `greedy` · `backtracking` · `binary-search` · `two-pointers` · `sliding-window` · `bit-manipulation` · `math` · `sorting` · `recursion` · `sql`

When a problem fits more than one, pick the category that matches the **core technique** used to solve it.

## Templates

- [`templates/template.py`](templates/template.py) — Python solution skeleton with a header docstring (source, difficulty, complexity).
- [`templates/template.cpp`](templates/template.cpp) — C++ competitive-programming skeleton with common macros and fast I/O.
- [`templates/explanation.md`](templates/explanation.md) — long-form write-up template, if a problem deserves more than a header comment.

## Adding a problem

1. Pick the right category.
2. Find the problem in that category's `exercises.md` (or add it to the list).
3. Create the solution file using the language template:
   - Python: `<category>/python/<problem-name>.py`
   - C++:    `<category>/cpp/<problem-name>.cpp`
4. Fill the header (source, difficulty, approach, complexity) before committing.

## Conventions

- Folder and file names: lowercase, **kebab-case** (`two-sum.py`, not `TwoSum.py`).
- One file per problem — the header docstring/comment **is** the write-up. Use [`templates/explanation.md`](templates/explanation.md) as a separate file only when the explanation is too long to fit in a header.
- Problem names use the canonical name only — no problem numbers, no platform prefixes.
- Commit messages: `<category>: <verb> <problem-name>`, e.g. `arrays: add two-sum`, `dp: refactor lis to O(n log n)`.
- Local scratch and binaries (`*.exe`, `input.txt`, `output.txt`, `scratch/`) are gitignored — never commit them.

## License

[MIT](LICENSE).
