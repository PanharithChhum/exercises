
###    Assignment   ###
#
# Your assignment is to implement the
# following function: `find_next_prime`.
# As the name states, given the number `n` the 
# function should return the next closest prime.
#
# Examples:
#  * `find_next_prime(6)` should return 7.
#  * `find_next_prime(10)` should return 11.
#  * `find_next_prime(11)` should return 13.
#
# You can use whatever you want (data structures,
# language features, etc).
# 
# Unit tests would be a plus.
#
### End Assignment  ###
 
import math, unittest

def find_next_prime(n):
    if n < 1:
        raise ValueError("number must be positive integer")
    next_num = n + 1
    while True:
        primes = True
        for x in range(2, int(math.sqrt(next_num)) + 1):
            if next_num % x == 0:
                primes = False
        if primes:
            return next_num
        next_num += 1

class TestFindNextPrime(unittest.TestCase):

    def test_7(self):
        self.assertEqual(find_next_prime(6), 7)

    def test_10(self):
        self.assertEqual(find_next_prime(10), 11)

    def test_11(self):
        self.assertEqual(find_next_prime(11), 13)

    def test_large_prime(self):
        self.assertEqual(find_next_prime(337), 347)

    def test_zero(self):
        self.assertRaises(ValueError, find_next_prime, 0)

    def test_negative_number(self):
        self.assertRaises(ValueError, find_next_prime, -1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindNextPrime)
    unittest.TextTestRunner(verbosity=2).run(suite)
