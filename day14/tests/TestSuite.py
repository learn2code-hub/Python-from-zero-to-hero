import unittest
from tests.EmployeeTests import EmployeeTests

test_loader = unittest.TestLoader()
another_suite = test_loader.loadTestsFromTestCase(EmployeeTests)
unittest.TextTestRunner().run(another_suite)
