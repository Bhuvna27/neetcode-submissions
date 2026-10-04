class Solution:
    def isHappy(self, n: int) -> bool:

        def sumOfSquares(n: int):
            output = 0

            while n > 0:
                remainder = n % 10
                output += remainder * remainder
                n //= 10

            return output

        slow = n
        fast = n

        while True:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False
        