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

# create class for GCD_calculator
class GCD_calculator:
    # calculate the greatest common divisor (GCD) of two numbers
    def calculate_gcd(self, a, b):
        # loop until the second number becomes zero
        while b != 0:
            temp = b  # temporarily hold the value of b
            b = a % b  # update b to remainder of divided by b
            a = temp  # update a to value of b before the remainder calculation
        return a  # return the GCD which is now stored in a

    # ask user input for two numbers and validate them
    def input_calculate(self):
        try:
            # prompt the user for the first number
            a = int(input("Enter first number: "))
            # prompt the user for the second number
            b = int(input("Enter second number: "))
            # Check if either number is negative
            if a < 0 or b < 0:
                raise ValueError("Enter positive number.")  # raise an error if it is negative number
            return a, b  # return the numbers
        except ValueError as e:  # handle exceptions related to invalid input
            print(f"Invalid input: {e}")  # print an error message
            return None, None  # return None for both numbers indicating an error


# create an instance of the GCD_calculator class
calculator = GCD_calculator()
# get user input for the two numbers using the input_calculate method
a, b = calculator.input_calculate()
# check if input values are valid
if a is not None and b is not None:
    # calculate and print the GCD of the two numbers
    print(f"GCD is", calculator.calculate_gcd(a, b))
