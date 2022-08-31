class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s.lower():
            if i.isalnum():
                a+=i
                
        return a==a[::-1]
        