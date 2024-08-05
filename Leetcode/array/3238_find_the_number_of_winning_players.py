class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        match={}
        for x in pick:
            if x[0] in match:
                match[x[0]].append(x[1])
            else:
                match[x[0]]=list()
                match[x[0]].append(x[1])
        res=0
        winning_keys = []
        for key,value in match.items():
            count_dic={}
            for x in value:
                if x in count_dic:
                    count_dic[x]+=1
                else:
                    count_dic[x]=1
            if any(count >= key + 1 for count in count_dic.values()):
                winning_keys.append(key)
        return len(winning_keys)
                
        print(match)
        return res
        
