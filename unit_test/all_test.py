import coverage
import unittest

from test_greatest_common_divisor import TestgreatestCommonDivisor

if __name__ == "__main__":
    cov = coverage.Coverage(include=["*/exercise/*"])

    cov.start()
    def Perform_testing():
        tests = unittest.TestSuite()
        tests.addTest(unittest.makeSuite(TestgreatestCommonDivisor))

        test_runner = unittest.TextTestRunner()
        test_runner.run(tests)
        cov.stop()
        cov.save()

        cov.html_report()
        exit()

    Perform_testing()