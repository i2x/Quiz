import unittest
from .functional_test import PollAppFunctionalTest as Test1
from .functional_test_private import PollAppFunctionalTest as Test2

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test1))
    test_suite.addTest(unittest.makeSuite(Test2))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
