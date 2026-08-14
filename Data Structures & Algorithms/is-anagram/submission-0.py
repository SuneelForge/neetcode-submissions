class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        
        fcount = [0] * 26
        for i in range(len(s)):
            fcount[ord(s[i]) - ord('a')] +=1
            fcount[ord(t[i]) - ord('a')] -=1

        for val in fcount:
            if val !=0 :
             return False
        return True