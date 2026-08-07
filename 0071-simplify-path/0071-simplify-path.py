class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for sym in path.split("/"):
            
            if sym == "..":
                if stack:
                  stack.pop()

            elif sym == "." or sym == "":
                continue

            else:
                stack.append(sym)

        return "/" + "/".join(stack)            


      

            


