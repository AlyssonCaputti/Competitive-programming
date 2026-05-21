# Heaps — Exercises

Solutions go in [`python/`](python/) and [`cpp/`](cpp/).

## Easy

1. **Kth Largest Element in a Stream** — maintain a min-heap of size `k`.
2. **Last Stone Weight** — repeatedly smash the two heaviest stones.
3. **Relative Ranks** — assign `Gold/Silver/Bronze/4th/...` by score.

## Medium

1. **Kth Largest Element in an Array** — quickselect or a size-`k` heap.
2. **Top K Frequent Elements** — heap on `(count, value)` pairs.
3. **K Closest Points to Origin** — max-heap of size `k` by squared distance.

## Hard

1. **Merge k Sorted Lists** — min-heap over the `k` list heads.
2. **Find Median from Data Stream** — two-heap online median.
3. **Sliding Window Maximum** — monotonic deque (or heap with lazy deletion).
