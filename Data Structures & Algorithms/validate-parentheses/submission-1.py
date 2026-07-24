class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        mp = {}
        mp['('] = ')'
        mp['{'] = '}'
        mp['['] = ']'        

        stack = []
        for char in s:
            if char in mp:
                stack.append(char)
            else:
                if not stack or mp[stack.pop()] != char:
                    return False
        
        return not stack