class Solution:

    def built(self,string):
        stack = []

        for ch in string:
            if ch != "#":
                stack.append(ch)
            elif stack:
                stack.pop()

        return stack            
    def backspaceCompare(self, s: str, t: str) -> bool:
        return True if self.built(s) == self.built(t) else False
      





        