class Solution:
    def myAtoi(self, s: str) -> int:
        i, n, sign, res = 0, len(s), 1, 0
        while i < n and s[i] == ' ':
            i += 1
        if i < n and s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        return max(-2**31, min(res, 2**31 - 1))