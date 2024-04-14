# Algorithm EuclideanAlgorithm(a, b)
#   Input: Two integers, a and b
#   Output: The greatest common divisor of a and b
#
#   while b ≠ 0
#     temp ← b
#     b ← a mod b
#     a ← temp
#   end while
#
#   return a
class GCD_calculator:
    def calculate_gcd(self, a, b):

        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


calculator = GCD_calculator()
print(calculator.calculate_gcd(48, 72))