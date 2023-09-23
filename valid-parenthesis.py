class Solution:
    def isValid(self, s: str) -> bool:
        b = ""
        for i in s:
            if i == "(":
                b += i
            if i == ")":
                if b[-1:] == "(":
                    b = b[:-1]
                else:
                    return False
            if i == "{":
                b += i
            if i == "}":
                if b[-1:] == "{":
                    b = b[:-1]
                else:
                    return False
            if i == "[":
                b += i
            if i == "]":
                if b[-1:] == "[":
                    b = b[:-1]
                else:
                    return False
        return not b