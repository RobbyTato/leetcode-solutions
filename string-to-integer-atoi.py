class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        signPassed = False
        sign = 1
        for i in s:
            if i == ' ' and not num and not signPassed:
                pass
            elif i in ('+', '-') and not num:
                if not signPassed:
                    if i == '+':
                        sign = 1
                    else:
                        sign = -1
                    signPassed = True
                else:
                    return 0
            elif i.isdigit():
                num += str(i)
            else:
                break
        if num:
            return max(min(int(num) * sign, 2147483647), -2147483648)
        return 0