class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        is_prime=None
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    is_prime=False
                    break  
            else:
                is_prime=True
        else:
            is_prime=True

        if is_prime:
            return n
        else:
            factor = 2
            output = 0 
        
            while n > 1:  
                while n % factor == 0:  
                    output += factor 
                    n //= factor  
                factor += 1  
            return output




        
