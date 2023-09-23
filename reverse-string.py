class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = s[:]
        length = len(temp)
        for i in range(length):
            s[-(i + 1)] = temp[i]