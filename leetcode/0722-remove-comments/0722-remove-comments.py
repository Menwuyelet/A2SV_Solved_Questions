"""
- The question: given a c++ code as list of lines, we are tasked to remove all the comments including line and block comments.
- Solution:
    - the approach i am taking for this problem is that to iterate through each line and process.
    - we have two states, in block and not in block.
    - taking the current line we evaluate the first two chrs of the line and check if they are the chr "/*" or "//" and wether we are in block or not.
    - if the chrs are "/*" and we are not in block, we change our state to in block and iterate through the line incrementing our ptr.
    - when processing block comment we might get multiple lines of comment so we check wether we are in block or not and if we are we do not start new line we treat it as one line even if we are on diffrent line.
    - when we hit "*/" we check if we are in block if we are we change our state to not in block. this marks the end of the block cmment.
    - if the chrs are "//" instead of "/*" we completly ignore that specific line completly and move to the next line.
    - if we are not in block and the first two chrs are not "//" the chr is not part of a comment rather it is code part so we add it to our single line temp variable.
    - after completing traversing one line we check if we have code lines in our temp variable and if so we append it to our ans.
    - after going throug all the lines we return the ans containing our conde lines.
-  Time and Space complexity:
    - Time = O(n * m), n = len(source), m = len(line)
    - space = O(n * m)
"""

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        ans = []
        for line in source:
            i = 0
            if not in_block:
                new_line = []
            
            # iterates through each line from our source and chcke the first two elements to decied.
            while i < len(line):
                if line[i:i+2] == "/*" and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == "*/" and in_block:
                    in_block = False
                    i += 1

                # if our first two chr are begining of line comment so the entire line will be removed.
                elif not in_block and line[i:i+2] == '//':
                    break

                # if we are not currently in block the current chr is part of the code not comment
                elif not in_block:
                    new_line.append(line[i])
            
                i += 1
            
            if new_line and not in_block:
                ans.append("".join(new_line))

        return ans
                
