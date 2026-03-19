"""
- The question: we are asked to print "Weird" if n (the input) is odd, even and between 6 adn 20(inclusive)
- else n (the input) is greater that 20, between 2 and 5(inclusive) print "Not Weird"
- Solution:
    - we are being asked to print "Weird" and "Not Weird" based on some conditions.
    - when we look at these condition we can see that only two conditions are there to print "Weird" the others all print "Not Weird"
    - so we do an if statment to print "Weird" checkin both conditions on single if statment by OR logical opration and print "Weird"
    - inside that condition. for other conditions we can just print "Not Weird"
-  Time and Space complexity:
    - Time = O(1)
    - space = O(1)

"""


def check(n):
    if n % 2 != 0 or n in range(6, 21):
        return "Weird"
    return "Not Weird"


if __name__ == "__main__":
    n = int(input().strip())

    print(check(n))
