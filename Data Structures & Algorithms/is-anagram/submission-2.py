class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        string1 = {}
        

        for char in range(len(s)):
            string1[s[char]] = string1.get(s[char],0)+1
            string1[t[char]] = string1.get(t[char],0)-1

        return all(v == 0 for v in string1.values())



        