import unittest
from parameterized import parameterized
from src.student import Student


class StudentTests(unittest.TestCase):

    @parameterized.expand([
        (2, 3, 5),
        (5, 2, 7),
        (-6, 6, 0),
        (-10_000_000, 5_000_000, -5_000_000),
    ])
    def test_given_two_integer_when_computeSum_is_called_then_sum_is_correct(self, a, b, r):
        # Arrange
        # x = 5
        # y = 9

        # Act
        result = Student.computeSum(a, b)

        # Assert
        self.assertEqual(r, result, "Compute sum doesn't work correctly")

    def test_given_specific_grades_when_computeAverage_is_called_then_the_average_is_truncated_to_two_decimals(self):
        grades = [9, 10, 10]
        student = Student(grades)

        average = student.computeAverage()

        self.assertEqual(9.66, average, "The average is not conform")

    def test_given_empty_list_when_computeAverage_is_called_then_the_method_should_raise_error(self):
        student = Student([])
        self.assertRaises(ZeroDivisionError, student.computeAverage)

if __name__ == "__main__":
    unittest.main()
