"""
Problem:    Climbing Stairs
Source:     LeetCode 70 — https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
Tags:       dynamic-programming, memoization, fibonacci

Approach:
    Each step n can be reached from step n-1 (taking 1 step) or from step n-2
    (taking 2 steps). So the total number of distinct ways to reach step n is
    ways(n) = ways(n-1) + ways(n-2), which is exactly the Fibonacci recurrence.

    Base cases: ways(1) = 1, ways(2) = 2.

    We use a bottom-up DP with O(1) space by keeping only the last two values.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

import sys


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


def solve() -> None:
    n = int(input())
    print(climb_stairs(n))


def main() -> None:
    input_data = sys.stdin.readline  # noqa: F841 — kept for consistency
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
