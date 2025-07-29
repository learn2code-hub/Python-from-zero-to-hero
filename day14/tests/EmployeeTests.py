import unittest
import json
from src.employee import Employee
from unittest.mock import patch

class EmployeeTests(unittest.TestCase):

    def test_employee_data(self):
        e = Employee()
        with patch("requests.get") as mocked_get:
            random_data = {"results": [{"name": {"first": "John", "last": "Smith"}}]}
            mocked_get.return_value.text = json.dumps(random_data)

            with patch("random.randint") as mocked_random:
                mocked_random.return_value = 5000

                e.get_placeholder()
                self.assertEqual("John Smith", e.name)
                self.assertEqual(e.salary, 5000)
                mocked_random.assert_called_with(1000, 10_000)
