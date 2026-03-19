"""
- The question: we are tasked to take two inputs and print them out back with formated string.
- Solution:
    - it is simple task we just use f"" string formater to print the formated string out.
-  Time and Space complexity:
    - Time = O(1)
    - space = O(1)
"""


def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")


if __name__ == "__main__":
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
