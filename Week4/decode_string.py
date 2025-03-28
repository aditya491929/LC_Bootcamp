class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                currStr = ""
                while stack and stack[-1] != "[":
                    currStr = stack.pop() + currStr

                stack.pop()

                currNum = ""
                while stack and stack[-1].isdigit():
                    currNum = stack.pop() + currNum

                string = int(currNum) * currStr

                stack.append(string)
            
        return "".join(stack)