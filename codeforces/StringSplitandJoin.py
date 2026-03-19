"""
- The question: we are asked to split a given string using white space as separator and join it back using - as connector
- Solution:
    - we shuold iterate throu the given string and replace white space by - every time we find it.
    - to do that we can use loop and iterate through it and since string is immutable we need to constract new string.
    - but in python we have two methods who can do that, split() and join()
    - we creat a list of the string spliting it by white space using split() method.
    - then we can join it back to string by - as connector using join() method.
    - this is more ifficient and standard than doing it using loop manualy.
-  Time and Space complexity:
    - Time = O(n) for split, O(n) for join, O(2n) for entire which is  O(n)
    - space = O(n+k) becuse of the list creation on split() k being the number of substrings created by the split process.
"""


def split_and_join(line):
    # write your code here
    splited_string = line.split(" ")
    return ("-").join(splited_string)


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
