#!/usr/bin/env python3

"""
Code copied from [1].

---

References:
    [1]: http://www.onlamp.com/pub/a/python/2004/12/02/tdd_pyunit.html
"""

import unittest

# Here's our "unit"
def IsOdd(n):
    return n % 2 == 1

# Here's out "unit tests"
class IsOddTests(unittest.TestCase):
    def testOne(self):
        self.failUnless(IsOdd(1))
    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
