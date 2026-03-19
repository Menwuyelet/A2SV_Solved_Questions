"""
- The question: we are given a string which is an out put of some keybard. the keyboard contains broken keys and if a key is broken it will type 2 times when pressed ones.
                - we are tasked to return the working keys. a key is either broken or not it wont be both once the started typing.
- Solution:
    - so this problem can be solved by using two pointers (parallel) checking if the two consiquetive chrs are the same.
    - if they are the same we ignore them and move our two pointers by two.
    - else the two are not the same we add the first in our working list and move our poiters by one to check the remainings.
    - we iterate until we reach the end.
    - after we reach the end we sort the list, remove duplicates and join it to string and return it.
-  Time and Space complexity:
    - Time => O(n), len(word)
    - space = O(n), if all the keys are working.
"""
for _ in range(int(input())):
    word = input()
    i = 0
    remaining = []

    while i < len(word):
        # to check if the two consiquetive chrs are equal and potentially be broken 
        if i + 1 < len(word) and word[i] == word[i + 1]:
            i += 2  
        else:
            remaining.append(word[i])
            i += 1

    # converts to set to remove duplicates and sort it to get it in order
    print("".join(sorted(set(remaining))))
