# Longest Happy String

## Problem Description

A string is called **happy** if it satisfies the following conditions:

- It only contains the letters `'a'`, `'b'`, and `'c'`.
- It does not contain any of the substrings `"aaa"`, `"bbb"`, or `"ccc"`.
- It contains at most `a` occurrences of the letter `'a'`, `b` occurrences of the letter `'b'`, and `c` occurrences of the letter `'c'`.

### Constraints
- `0 <= a, b, c <= 100`
- `a + b + c > 0`

### Examples

**Example 1:**
```python
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
