class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_tab_array = [0]*26
        for i in range(len(s)):
            hash_tab_array[ord(s[i]) - ord('a')] +=1
            hash_tab_array[ord(t[i]) - ord('a')] -=1
        
        for i in hash_tab_array:
            if i !=0:
                return False
        return True