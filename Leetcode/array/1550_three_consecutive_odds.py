class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_list=[]
        max_count=0
        for i in range(len(arr)):
            if arr[i]%2!=0:
                odd_list.append(arr[i])
                if(len(odd_list)==3):
                    return True
            else:
                odd_list.clear()
                pass

        print(odd_list)
        return False
