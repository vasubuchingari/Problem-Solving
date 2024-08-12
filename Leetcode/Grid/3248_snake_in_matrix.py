class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        k=0
        matrix=[]
        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append(k)
                k=k+1
            matrix.append(temp)
        print(matrix)

        i,j=0,0
        for x in commands:
            if x=="RIGHT":
                j=j+1
            elif x=="LEFT":
                j=j-1
            elif x=="UP":
                i=i-1
            elif x=="DOWN":
                i=i+1
        return(matrix[i][j])
        
