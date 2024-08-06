class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for x in strs:
            sorted_x=tuple(sorted(x))
            if sorted_x not in anagrams:
                anagrams[sorted_x]=[]
            anagrams[sorted_x].append(x)
        print(anagrams)
        return (list(anagrams.values()))
