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

    def input_calculate(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return self.calculate_gcd(a, b)

calculator = GCD_calculator()
result = calculator.input_calculate()
print(f"GCD is {result}")