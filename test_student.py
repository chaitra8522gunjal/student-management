
import unittest

from student import add_student, get_result


class TestStudentManagement(unittest.TestCase):

    def test_student_can_be_added(self):
        student = add_student("Riya", 85)

        self.assertEqual(student["name"], "Riya")
        self.assertEqual(student["marks"], 85)

    def test_student_passes(self):
        self.assertEqual(get_result(85), "Pass")

    def test_student_fails(self):
        self.assertEqual(get_result(28), "Fail")

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            get_result(120)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            add_student("   ", 50)


if __name__ == "__main__":
    unittest.main()
