import coverage
import unittest

if __name__ == "__main__":
    cov = coverage.Coverage(include=["*/exercise/*"])

    cov.start()
    def Perform_testing():
        tests = unittest.TestSuite()

        test_runner = unittest.TextTestRunner()
        test_runner.run(tests)
        cov.stop()
        cov.save()

        cov.html_report()
        exit()

    Perform_testing()