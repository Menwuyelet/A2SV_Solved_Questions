"""
- The question: we are given a string path we are tasked to minimalise it to simplified canonical file path
- Solution:
    - what we really want to do is to remove directories just befor "..", remove duplicate slash, remove a referance to the current directory "." and remove any slash at the end of the path.
    - to do that we can use a stack so we can remove a directory just before "..".
    - we create a list by spliting the path by "/" so we get only the directory names and ".." or "." comands removing all the slashs.
    - after that we iterate through the the list and append the directory name and pop a directory name if the current element is ".." else if it is "." we just continue without doing anything.
    - after we create the stack with final directory names we join them using slash to make it valid path.
    - after that we add one last slash at the bigining of the path to make it valid. 
-  Time and Space complexity:
    - Time = O(n), n = length of the given path due to the split 
    - space = O(n)
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []

        for word in paths:
            # if the current word is a comand to go back we check that the stack is not empty to pop
            if word == ".." and stack:
                stack.pop()

            # if we need to go back and the stack is empty or the word in our stack is just empty string or the word in our stack is refering to the current directory we just continue with out doing anything
            elif word == ".." or word == "" or word == ".":
                continue
            else:
                stack.append(word)
        
        # we join our stack back using slach to create the path and we add one additional slash to represent the home directory toelse it will be like home/foo when it should be /home/foo. 
        ans = "/" + "/".join(stack)

        return ans