"""
- The question: we are given a list of integers that represent a bill notes and we are tasked to determine if we can sell them 1 lemonade and provide them with theire change.
- Solution:
    - the problem seems easy like just accumulate all the money we have and if we have larger money than the required change we clould just return true.
    - but the trick or the part we tend to forget is that the money notes we have matter.
    - meaning if we have 20 ammount of money but with two 10 notes we cant give a change to 20 note giving customer.
    - so to solve this we should keep track of the amount of notes we have for each the two notes 5 and 10.
    - and if the given bill is 5 we just add it to our five bill count, if 10 we check if we have enough 5 notes and if 20 we check if we have enough 10s and 5s note or only enough 5s note.
    - if we dont have enough we return False else we return True at the end of the iteration.
-  Time and Space complexity:
    - Time = O(n), n = len(bills)
    - space = O(1), 
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        # we iterate over the list of bills and check for each bill.
        for bill in bills:

            # if our current bill is 5 we just add 1 to our five bill count
            if bill == 5:
                fives += 1
            
            # if our bill is 10 we check if we have enugh 5 bills to give change and add 1 to our ten bill counter and subtract 1 from our 5 bill counter.
            # else we return false even if we have more 10 bills
            elif bill == 10:
                if fives:
                    fives -= 1
                    tens += 1

                else:
                    return False

            # if our bill is 20 we check wether we have enough of both 10s and 5s or only enough of 5s and do the same thing.
            else:

                # we check if enough of both 10s and 5s
                if tens and fives:
                    tens -= 1
                    fives -= 1

                # we check if enough of only 5s
                elif fives >= 3:
                    fives -= 3

                else:
                    return False
                
        # we return true at the end since we gave changes to all customers
        return True