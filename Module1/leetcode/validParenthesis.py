#https://leetcode.com/problems/valid-parentheses/submissions/1528958961/

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if (i=='(' or i=='{' or i=='['):
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if (i==')') :
                    if(stack[-1]=='('):
                        stack.pop()
                    else :
                        return False
                if (i==']') :
                    if(stack[-1]=='['):
                        stack.pop()
                    else :
                        return False
                if (i=='}') :
                    if(stack[-1]=='{'):
                        stack.pop()
                    else :
                        return False
        if len(stack)>0:
            return False
        
        return True