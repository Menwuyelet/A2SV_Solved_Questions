"""
- The question: we are tasked to calculate the power(square of number a to number b) of the first two numbers form the input and calculate
              - the mode of that number (the result of first task) to the third number from the input.
- Solution:
    - To do this we can manually campute the power using ** oprator and then mode it using % oprator.
    - but there is also another way wchich utilizes the biult in function pow().
    - pow() can take up to 3 arguments and when we give it 3 argument it calculates the first number raised to the second number and
    - then mode it to the third number and return one number.
    - so we can use it to perform both tasks.
-  Time and Space complexity:
    - Time = O(log b) due to pow(a,b)
    - space = O(log m) due to pow(a, b, m)
"""

a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))
