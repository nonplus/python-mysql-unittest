import unittest
from datetime import date
import mysql.connector
import os
import re
from models import Student
from db import Datastore


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Connect to test mysql database
        self.connection = mysql.connector.connect(
            user='test', database='testdb', password='test')
        # Initialize mysql database for testing
        self.execute_sql_script(os.path.join(
            os.path.dirname(__file__), 'test_setup.sql'))
        # Instantiate datastore 
        self.datastore = Datastore(self.connection)

    def test_insert_student_inserts_student(self):
        # Exercise
        student = self.datastore.insert_student(
            Student(name='Alice', dob=date(2010, 12, 25), grade=5))

        # Verify
        self.assertEqual(student, self.datastore.list_students()[0])

    def test_list_students_returns_all_students(self):
        # Setup
        student1 = self.datastore.insert_student(
            Student(name='Alice', dob=date(2010, 12, 25), grade=5))
        student2 = self.datastore.insert_student(
            Student(name='Bob', dob=date(2010, 3, 13), grade=2))
        
        # Exercise
        students = self.datastore.list_students()

        #Verify
        self.assertEqual(students, [student1, student2])

    def tearDown(self):
        self.connection.close()

    # Execute the sql statements in the specified file
    def execute_sql_script(self, file_path):
        f = open(file_path, mode='r')
        statements = [sql for sql in re.split(';\\n', f.read(), re.M)]
        f.close()
        cursor = self.connection.cursor()
        for statement in statements:
            # Remove comments
            statement = re.sub('--.*$', '', statement, 0, re.M)
            if (re.search('\w', statement)):
                # Execute non-empty command
                cursor.execute(statement)
        cursor.close()


if __name__ == '__main__':
    unittest.main()
