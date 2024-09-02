class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        i=0
        while i < len(s):
            st = ""
            while i < len(s) and s[i] is not " ":
                st = st + s[i]
                i = i + 1
            if st != "":
                l.append(st)
            while i<len(s) and s[i]==" ":
                i=i+1
        return " ".join(l[::-1])

