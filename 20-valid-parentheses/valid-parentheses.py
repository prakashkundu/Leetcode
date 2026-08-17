class Solution(object):
    def isValid(self, s):
        stack = []
        dic = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in dic:                   
                if not stack or stack.pop() != dic[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack)==0                            