class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")

        v1=list(map(int,v1))
        v2=list(map(int,v2))
        
        max_len=max(len(v1),len(v2))

        for i in range(max_len):
            v1i=v1[i] if i<len(v1) else 0
            v2i=v2[i] if i<len(v2) else 0
            if v1i>v2i:
                return 1
            elif v2i>v1i:
                return -1

        return 0

        
