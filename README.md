# Competitive Programming

A personal collection of algorithm and data-structure problems I've worked through, organized by topic. Each problem lives in its own folder with the solution and a short write-up explaining the approach.

The point of this repo isn't to chase problem count — it's to keep a clean record of how I think about each problem so I can revisit it later and so anyone reading can follow along.

---

## How it's organized

Problems are grouped into category folders at the root. Inside each category, every problem gets its own folder containing the solution file and an explanation.

```
competitive-programming/
├── arrays/
├── strings/
├── hashmaps/
├── linked-lists/
├── stacks-and-queues/
├── trees/
├── graphs/
├── heaps/
├── dynamic-programming/
├── greedy/
├── backtracking/
├── binary-search/
├── two-pointers/
├── sliding-window/
├── bit-manipulation/
├── math/
├── sorting/
├── recursion/
├── sql/
└── templates/
```

### Example

```
arrays/
└── two-sum/
    ├── solution.<ext>
    └── explanation.md
```

The `<ext>` is whatever language the solution is written in (`cpp`, `py`, `js`, `java`, `sql`, etc.). If a problem has multiple solutions in different languages, append the language to the filename:

```
arrays/
└── two-sum/
    ├── solution.cpp
    ├── solution.py
    └── explanation.md
```

---

## Categories

| Category | What goes here |
|---|---|
| `arrays/` | Problems centered on array manipulation, traversal, in-place updates |
| `strings/` | String parsing, pattern matching, character-level logic |
| `hashmaps/` | Frequency counting, lookup-based problems, set operations |
| `linked-lists/` | Singly/doubly linked list traversal, reversal, cycle detection |
| `stacks-and-queues/` | Stack-based parsing, monotonic stacks, queue/deque problems |
| `trees/` | Binary trees, BSTs, traversals, tree DP |
| `graphs/` | BFS, DFS, shortest path, topological sort, union-find |
| `heaps/` | Priority queue problems, top-k, scheduling |
| `dynamic-programming/` | 1D/2D DP, memoization, tabulation |
| `greedy/` | Interval problems, scheduling, exchange-argument proofs |
| `backtracking/` | Permutations, combinations, N-queens-style search |
| `binary-search/` | Sorted array search, binary search on answer |
| `two-pointers/` | Pair-finding, in-place partition, sorted-array techniques |
| `sliding-window/` | Subarray/substring problems with a moving window |
| `bit-manipulation/` | XOR tricks, bitmask DP, bit-counting |
| `math/` | Number theory, combinatorics, geometry |
| `sorting/` | Custom comparators, sort-based reductions |
| `recursion/` | Pure recursion patterns that don't fit DP or backtracking |
| `sql/` | SQL query challenges (LeetCode, HackerRank, etc.) |

A problem sometimes fits in more than one bucket. Pick the category that best matches the **core technique** used in the solution, not the surface description.

---

## Adding a new problem

1. Pick the category that matches the core technique.
2. Create a folder using **kebab-case**, named after the problem:
   ```
   arrays/maximum-subarray/
   ```
3. Drop in `solution.<ext>` and `explanation.md` (copy from `templates/explanation.md`).
4. Fill in the explanation before committing — even a few lines is better than nothing.

---

## Naming conventions

- **Folders:** lowercase, kebab-case → `dynamic-programming/`, `longest-common-subsequence/`
- **Problem folders:** use the problem's canonical name from the source, in kebab-case. Don't include the problem number or platform prefix.
  - ✅ `two-sum/`
  - ❌ `1-two-sum/`, `lc_two_sum/`, `TwoSum/`
- **Solution files:** always `solution.<ext>`. The extension identifies the language.
- **Explanation file:** always `explanation.md`.
- **Multiple languages:** keep both files side-by-side: `solution.cpp`, `solution.py`.

---

## Commit style

Short, descriptive, present-tense. Prefix with the category so history is easy to scan:

```
arrays: add two-sum
graphs: add course-schedule with topo-sort write-up
dp: refactor longest-increasing-subsequence to O(n log n)
docs: clarify category guidelines in README
```

One commit per problem is the default. Group commits only when the changes genuinely belong together (e.g. a write-up fix plus a small solution tweak).

---

## Maintenance rules

- **One problem, one folder.** Never put two problems in the same folder.
- **Explanation is not optional.** If there's a `solution.<ext>`, there's an `explanation.md` next to it.
- **Don't break existing folders.** If you rename a problem, rename the folder to match — don't leave dead names.
- **Keep the root clean.** No loose solution files at the root, no scratch files committed by accident.
- **Source attribution.** If the problem comes from LeetCode, HackerRank, Codeforces, etc., mention it in the explanation, not the folder name.

---

## License

Personal study repo. Solutions are my own work unless explicitly noted in the explanation.
