class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []

        for word in paths:
            if word == ".." and stack:
                stack.pop()
        
            elif word == ".." or word == "" or word == ".":
                continue
            else:
                stack.append(word)
        
        ans = "/".join(stack)
        ans = "/" + ans

        return ans