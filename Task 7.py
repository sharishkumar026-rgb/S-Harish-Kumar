from abc import ABC, abstractmethod
from functools import reduce

# Task 2 Abstraction
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# Base Class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


#  Task 1 super()
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


#  DATA CREATION

students = [
    Student("Harish", 1, "CA", 60000),
    Student("Arun", 2, "CS", 40000),
    Student("Vijay", 3, "IT", 80000)
]

faculty = [
    Faculty("Ravi", 101, 35000),
    Faculty("Suresh", 102, 25000),
    TempFaculty("Kumar", 103, 30000, "6 months")
]

# Task 3 Sorting
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

# Task 4 map()

student_names = list(map(lambda s: s.name, students))

# Task 5 filter()

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

# Task 6 reduce()
# -------------------------------
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

# Task 7: Higher Order Function

def process_users(users, func):
    return list(map(func, users))

#  FINAL OUTPUT

print("----- ALL DETAILS -----")
for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())

print("\n----- SORTED STUDENTS (by fees) -----")
for s in students:
    print(s.name, s.fees)

print("\n----- SORTED FACULTY (by salary) -----")
for f in faculty:
    print(f.name, f.salary)

print("\n----- STUDENT NAMES (map) -----")
print(student_names)


print("\n----- HIGH FEE STUDENTS (filter) -----")
for s in high_fee_students:
    print(s.name, s.fees)


print("\n----- HIGH SALARY FACULTY (filter) -----")
for f in high_salary_faculty:
    print(f.name, f.salary)

print("\n----- TOTAL FEES (reduce) -----")
print(total_fees)

print("\n----- TOTAL SALARY (reduce) -----")
print(total_salary)

print("\n----- USING HIGHER ORDER FUNCTION -----")
names_upper = process_users(students, lambda s: s.name.upper())
print(names_upper)