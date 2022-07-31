class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        x = str(x)  #TC?
        d = len(x)-1
        for i in range(d//2+1):
            if x[i] != x[d-i]:
                return False
        return True
        """
        
        # Solving without turning the integer into a string
        if x < 0:
            return False
        if x >= 10 and x % 10 == 0:
            return False
        
        reversed = 0
        # this is how we can check up until 'halfway'
        while x > reversed:
            reversed = reversed*10 + x%10
            x = x // 10
            
        # check for both even and odd palindromes
        return x == reversed or x == reversed//10