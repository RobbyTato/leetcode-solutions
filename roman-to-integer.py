class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                ans += 1
            elif s[i] == "V":
                if len(s) - 1 > i and s[i + 1] == "I":
                    i += 1
                    ans += 4
                else:
                    ans += 5
            elif s[i] == "X":
                if len(s) - 1 > i and s[i + 1] == "I":
                    i += 1
                    ans += 9
                else:
                    ans += 10
            elif s[i] == "L":
                if len(s) - 1 > i and s[i + 1] == "X":
                    i += 1
                    ans += 40
                else:
                    ans += 50
            elif s[i] == "C":
                if len(s) - 1 > i and s[i + 1] == "X":
                    i += 1
                    ans += 90
                else:
                    ans += 100
            elif s[i] == "D":
                if len(s) - 1 > i and s[i + 1] == "C":
                    i += 1
                    ans += 400
                else:
                    ans += 500
            elif s[i] == "M":
                if len(s) - 1 > i and s[i + 1] == "C":
                    i += 1
                    ans += 900
                else:
                    ans += 1000
            i += 1
        return ans