class Solution:
    def fib(self, n: int) -> int:
        fibs = {}
        def fib(n):
            a = 0
            if n <2:
                fibs[n]=a
                return n
                
            else:
                #chaek >.. valu return
                if n in fibs:
                    return fibs[n]
                else:
                    
                    fibs[n] = fib(n-1)+fib(n-2)
                    return fibs[n]
        return fib(n)