#imp
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        longest=0
        l=0
        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[l])
                l=l+1
            sett.add(s[i])
            longest=max(longest,i-l+1)
        return longest
        
