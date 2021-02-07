from stack import Stack

def is_match(p1,p2):
        if p1=='(' and p2==')':
            return True
        elif p1=='{' and p2=='}':
            return True 
        elif p1=='[' and p2==']':
            return True
        else:
            return False
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        index = 0
        is_balanced = True
        while index<len(s) and is_balanced:
            curr = s[index]
            if curr in '({[':
                stack.push(curr)
            else:
                if stack.is_empty():
                    is_balanced = False
                else:
                    top = stack.pop()
                    if not is_match(top,curr):
                        is_balanced = False
            index+=1
        if stack.is_empty() and is_balanced:
            return True
        else:
            return False
        
