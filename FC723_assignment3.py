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
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            if a < 0 or b < 0:
                raise ValueError("Enter positive number.")
            return a, b
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None, None


calculator = GCD_calculator()
a, b = calculator.input_calculate()
if a is not None and b is not None:
    print(f"GCD is", calculator.calculate_gcd(a, b))