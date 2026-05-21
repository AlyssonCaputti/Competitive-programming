# SQL — Exercises

Solutions go in this folder as `.sql` files (single language — no `python/` or `cpp/`).

## Easy

1. **Combine Two Tables** — `LEFT JOIN` `Person` with `Address`, returning all people.
2. **Employees Earning More Than Their Managers** — self-join on manager id.
3. **Duplicate Emails** — `GROUP BY email HAVING COUNT(*) > 1`.

## Medium

1. **Department Highest Salary** — per department, employees with the top salary.
2. **Exchange Seats** — swap adjacent student pairs, leaving the last alone if odd.
3. **Rank Scores** — dense rank with `DENSE_RANK()` (no gaps).

## Hard

1. **Trips and Users** — cancellation rate per day, excluding banned users.
2. **Human Traffic of Stadium** — three or more consecutive days with `people >= 100`.
3. **Department Top Three Salaries** — top three distinct salaries per department.
