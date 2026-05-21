# Competitive Programming

My solutions to algorithm and data-structure problems, grouped by topic. Each problem has its own folder with the code and a short write-up of how I approached it.

## Structure

```
<category>/<problem-name>/
    ├── solution.<ext>
    └── explanation.md
```

Example:

```
arrays/two-sum/
    ├── solution.py
    └── explanation.md
```

If I solve the same problem in more than one language, both files live side-by-side: `solution.cpp`, `solution.py`.

## Categories

`arrays` · `strings` · `hashmaps` · `linked-lists` · `stacks-and-queues` · `trees` · `graphs` · `heaps` · `dynamic-programming` · `greedy` · `backtracking` · `binary-search` · `two-pointers` · `sliding-window` · `bit-manipulation` · `math` · `sorting` · `recursion` · `sql`

When a problem fits more than one, I pick the category that matches the **core technique** I used to solve it.

## Adding a problem

1. Find the right category.
2. Create a folder in kebab-case: `arrays/maximum-subarray/`.
3. Add `solution.<ext>` and `explanation.md` (template lives in [`templates/`](templates/explanation.md)).
4. Fill in the write-up before committing.

## Conventions

- Folders and files: lowercase, kebab-case.
- Problem folders use the canonical name only — no problem numbers, no platform prefixes.
- Solution file is always `solution.<ext>`; write-up is always `explanation.md`.
- Commit messages look like `arrays: add two-sum` or `dp: refactor lis to O(n log n)`.
- One problem per folder. One explanation per solution. No loose files at the root.
