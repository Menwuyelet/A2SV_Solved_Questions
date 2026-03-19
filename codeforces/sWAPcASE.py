"""
- The question: for each alphabet in the given string swap their case. if it was capital letter convert it to smalle and vice versa
- Solution:
    - in order to tell if a charachters case the charachter should be alphabet (a-z).
    - we traverse through the given string and check if the chrachter is alphabet (a-z) or not,
    - if so we check its case and swap it to the opposite and add it to our result string.
    - else we simply add it to our result string.
- Time and Space complexity:
    - Time = O(n) as we iterate throug the entire string
    - space = O(1)
"""


def swap_case(s):
    changedS = ""
    for chr in s:
        if chr.isalpha():
            chr = chr.upper() if chr.islower() else chr.lower()
        changedS += chr
    return changedS


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
