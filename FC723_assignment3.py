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
