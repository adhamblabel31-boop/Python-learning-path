# ----------------------------------------------------
# ! ----------- unit testing with unittest -----------
# ----------------------------------------------------
# todo# test runner
# ? the module that run the unit testing (unittest, pytest)
# ----------------------------------------------------
# todo# test case
# ? smallest unit of testing
# ? it use asserts methods to check for actions and responses
# todo# test suite
# ? collection of multiple tests or test cases
# todo# test report
# ? a full report contains the failure or succeed
# ----------------------------------------------------
# todo# unittest
# ? add tests into classes as methods
# ? use a series of special assertion methods
# ? https://docs.python.org/3/library/unittest.html
# ----------------------------------------------------

import unittest

# print(dir(unittest))

# assert 3 * 3 == 9, "should be 9"

# def test1():
#     assert 3 * 3 == 9, "should be 9"

# def test2():
#     assert 5 * 5 == 25, "should be 25"

# if __name__ == "__main__":
#     test1()
#     test2()
#     print("all tests passed")


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(100 > 99, "should be true")

    def test2(self):
        self.assertEqual(3 * 3, 9, "should be 9")

    def test3(self):
        self.assertGreater(100, 99, "should be true")


if __name__ == "__main__":
    unittest.main()
