from model import Student
from dataclasses import replace

# Class providing access to the database


class Datastore:
    def __init__(self, connection) -> None:
        self.connection = connection

    def insert_student(self, student) -> Student:
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO Student (Name, DOB, Grade, GPA) VALUES (%s, %s, %s, %s)", (
                student.name, student.dob, student.grade, student.gpa))
            return replace(student, id=cursor.lastrowid)
        finally:
            cursor.close()

    def list_students(self) -> list[Student]:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT ID, Name, DOB, Grade, GPA FROM Student ORDER BY ID")
            return [Student(id=row[0], name=row[1], dob=row[2], grade=row[3], gpa=row[4]) for row in list(cursor)]
        finally:
            cursor.close()
