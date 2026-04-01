# Task 1 Task 1: Encapsulation (User Class)
class User:
    def __init__(self):
        self.__user_name = None   # private variable
        self.__pwd = None         # private variable

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   # password hidden

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


# Test
u = User()
u.set_user("john", "1234")
u.register()
u.login()

# Task 2: Inheritance (User → Student, Faculty, TempFaculty)

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged in")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):   # Multilevel inheritance
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Test
s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.register()
t.faculty_greet()
t.tempFaculty_greet()

# Task 3 Method Overriding

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):   # overriding
        print("Welcome Student")


class Faculty(User):
    def greet(self):   # overriding
        print("Welcome Faculty")


# Test
s = Student()
s.greet()

f = Faculty()
f.greet()

# Task 4 Method Chaining

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# Test
user = User()
user.login().greet().register()

# Task 5 Combined Real Time System

class User:
    users_count = 0   # class variable

    def __init__(self, username, pwd):
        self.__username = username
        self.__pwd = pwd
        User.users_count += 1

    def get_user(self):
        return self.__username

    def register(self):
        print(f"{self.__username} registered")
        return self

    def login(self):
        print(f"{self.__username} logined")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):   # override
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):   # override
        print("Welcome Faculty")
        return self


# Test
s1 = Student("john", "123")
s1.login().greet().register()

f1 = Faculty("admin", "999")
f1.login().greet().register()

print("Total Users:", User.users_count)