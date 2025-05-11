import csv
import pickle
from functools import cmp_to_key


class Student:
    def __init__(self, surname: str, musical_instrument: str):
        # Let's think of it as a primary key. Yeah...
        self.surname = surname.capitalize()
        self.musical_instrument = musical_instrument.capitalize()

    def __repr__(self):
        return f"{self.surname}"

    @staticmethod
    def init_by_stdin():
        surname = input("Enter surname of the student: ")
        musical_instrument = input(
            "Enter the name of musical instrument of a user: ")
        student = Student(
            surname=surname, musical_instrument=musical_instrument)
        print(
            f"Student {student.surname} plays {student.musical_instrument}")


class Speciality:
    def __init__(self, name: str, allowed_instruments: list[str]):
        self.name = name.capitalize()
        self.allowed_instruments = [x.capitalize()
                                    for x in allowed_instruments]


class CsvMixin:
    def SaveExamsToCsv(self, dicts: list[Speciality], filename):
        with open(filename, "w") as filename:
            writer = csv.DictWriter(filename, fieldnames=[
                                    "name", "allowed_instruments", "belonging_students"])
            writer.writeheader()
            for dict in dicts:
                writer.writerow({"name": dict.name, "allowed_instruments": dict.allowed_instruments,
                                "belonging_students": {x.surname for x in dict.belonging_students}})

    def GetStudentsAssignedFromCsv(self, filename: str):
        with open(filename, "w") as filename:
            reader = csv.DictReader(filename, fieldnames=[
                                    "name", "allowed_instruments", "belonging_students"])
            names = []
            for row in reader:
                names.append({row["name"]: row["belonging_students"]})

            print(names)


class PickleMixin:
    def SaveExamsToPickle(self, dicts: list[dict[any]], filename):
        with open(filename, "wb") as file:
            for dict in dicts:
                pickle.dump([dict.__dict__ for dict in dicts], file)

    def GetAllFromPickle(self, filename: str):
        with open(filename, "rb") as filename:
            result_list = []
            result_list = pickle.load(filename)
            print(result_list)


HARDCODED_EXAMS_LIST = [{"name": "Solphejio", "allowed_instruments": [
    "piano", "guitar"]}, {"name": "choir", "allowed_instruments": ["triangle", "violin"]}]
HARDCODED_STUDENTS_LIST = [{"surname": "Ivanov", "musical_instrument": "triangle"}, {
    "surname": "Petrov", "musical_instrument": "guitar"}, {"surname": "Tarkovski", "musical_instrument": "guitar"}, {"surname": "Bubnov", "musical_instrument": "violin"}]
PICKLE_FILENAME = "/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR4/txt_sources/participators.pck"
CSV_FILENAME = "/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR4/txt_sources/participators.csv"


class Saver(CsvMixin, PickleMixin):
    def SortByExams(self, exams: list[dict[str]], students: list[dict[str]]):
        belongingStudents = set()
        examsList = []
        for exam in exams:
            exam = Speciality(exam["name"], exam["allowed_instruments"])
            for student in students:
                student = Student(student["surname"],
                                  student["musical_instrument"])
                if (student.musical_instrument in exam.allowed_instruments):
                    belongingStudents.add(student)
            exam.belonging_students = list(belongingStudents)
            examsList.append(exam)
            belongingStudents = set()
            sorted(examsList, key=lambda exam: exam.name)
        self.SaveExamsToCsv(
            examsList,   CSV_FILENAME)
        self.SaveExamsToPickle(
            examsList, PICKLE_FILENAME)

    def SearchStudentExamsFromCsv(self, surname: str, filename: str):
        with open(filename, "r") as filename:
            reader = csv.DictReader(filename, fieldnames=[
                                    "name", "allowed_instruments", "belonging_students"])
            exams = []
            for row in reader:
                if surname in row["belonging_students"]:
                    exams.append(row["name"])
        print(exams)

    def GetAllFromCsv(self, filename: str):
        header_vals = ["name", "allowed_instruments", "belonging_students"]
        with open(filename, "r") as filename:
            reader = csv.DictReader(filename, fieldnames=header_vals)
            header_row = {x: x for x in header_vals}
            exams = []
            for row in reader:
                if not row == header_row:
                    exams.append(row)
        print(exams)


def solve_task_1():
    saver = Saver()
    saver.SortByExams(HARDCODED_EXAMS_LIST, HARDCODED_STUDENTS_LIST)
    user_input = ''
    while user_input != 0:
        while user_input is not int:
            user_input = input(
                "Enter the wanted operation: \n0) Exit subroutine \n1) get exams list by surname \n2) read available exams info from csv \n3) do the same, but from pickle\n")
            try:
                user_input = int(user_input)
                if user_input < 0 or user_input > 3:
                    raise ValueError
                break
            except ValueError:
                print("Enter valid operation num")
        if user_input == 1:
            user_input = input("Enter surname of student: ")
            saver.SearchStudentExamsFromCsv(user_input, CSV_FILENAME)
        if user_input == 2:
            saver.GetAllFromCsv(CSV_FILENAME)
        if user_input == 3:
            saver.GetAllFromPickle(PICKLE_FILENAME)


def main():
    solve_task_1()


if __name__ == "__main__":
    main()
