# Mini Project 1: Employee Management System

employees = []

def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    
    emp = {"name": name, "age": age, "role": role, "salary": salary}
    employees.append(emp)

def display():
    for emp in employees:
        print(emp)

def update_employee(name):
    for emp in employees:
        if emp["name"] == name:
            emp["salary"] = float(input("Enter new salary: "))
            print("Updated!")

def delete_employee(name):
    global employees
    employees = [emp for emp in employees if emp["name"] != name]

    # Menu
while True:
    print("1.Add 2.Update 3.Delete 4.Display 5.Exit")
    ch = input("Choose: ")

    if ch == "1":
        add_employee()

    elif ch == "2":
        name = input("Enter name to update: ")
        update_employee(name)

    elif ch == "3":
        name = input("Enter name to delete: ")
        delete_employee(name)

    elif ch == "4":
        display()

    elif ch == "5":
        break

    else:
        print("Invalid choice\n")

# Mini Project 2: Student Report Card

def report_card():
    name = input("Enter student name: ")
    m1 = int(input("Marks 1: "))
    m2 = int(input("Marks 2: "))
    m3 = int(input("Marks 3: "))
    
    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 90: grade = "A"
    elif avg >= 75: grade = "B"
    elif avg >= 50: grade = "C"
    else: grade = "Fail"

    print(f"\nReport Card for {name}")
    print(f"Total: {total}, Average: {avg:.2f}, Grade: {grade}")

report_card()

# Mini Project 3: Shopping Cart System

cart = []

def add_item():
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    cart.append({"name": name, "price": price, "qty": qty})

def remove_item():
    name = input("Enter product to remove: ")
    global cart
    cart = [item for item in cart if item["name"] != name]

def display_cart():
    total = 0
    for item in cart:
        subtotal = item["price"] * item["qty"]
        total += subtotal
        print(f"{item['name']} - {item['qty']} x {item['price']} = {subtotal}")
    print("Total:", total)

while True:
    print("1.Add 2.Remove 3.Display 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_item()

    elif ch == "2":
        remove_item()

    elif ch == "3":
        display_cart()

    elif ch == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!\n")

# Mini Project 4: Login & User Validation

users = {"admin": "1234", "user": "abcd"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid credentials!")

# Mini Project 5: Unique Visitor Counter

visitors = set()

while True:
    name = input("Enter visitor name (or 'exit'): ")
    if name == "exit":
        break
    visitors.add(name)

print("Unique visitors:", len(visitors))
print(visitors)

# Mini Project 6: String Formatter Tool

name = input("Enter your name: ")
product = input("Enter product: ")

print(f"{name} purchased {product}")

print("Left aligned :", name.ljust(20, "*"))
print("Right aligned:", name.rjust(20, "*"))
print("Center aligned:", name.center(20, "*"))

# Mini Project 7: Bank Account System

account = {}

def create_account():
    name = input("Enter name: ")
    balance = float(input("Enter balance: "))
    account["name"] = name
    account["balance"] = balance

def deposit():
    amount = float(input("Enter amount: "))
    account["balance"] += amount

def withdraw():
    amount = float(input("Enter amount: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
    else:
        print("Insufficient balance!")

def check_balance():
    print("Balance:", account["balance"])

create_account()

while True:
    print("1.Deposit 2.Withdraw 3.Check 4.Exit")
    ch = input("Choice: ")
    if ch == "1": deposit()
    elif ch == "2": withdraw()
    elif ch == "3": check_balance()
    elif ch == "4": break

# Mini Project 8: Voting System

votes = {"A": 0, "B": 0, "C": 0}

while True:
    vote = input("Vote (A/B/C or exit): ")
    if vote == "exit":
        break
    if vote in votes:
        votes[vote] += 1

winner = max(votes, key=votes.get)
print("Winner is:", winner)

# Mini Project 9: Course Enrollment System

students = {}

def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(",")
    students[name] = courses
    print("Student added!\n")

def update_courses():
    name = input("Enter student name: ")
    if name in students:
        students[name] = input("New courses: ").split(",")
        print("Courses updated!\n")
    else:
        print("Student not found!\n")

def display():
    if not students:
        print("No students found!\n")
        return

    for k, v in students.items():
        print(k, ":", v)
    print()

while True:
    print("1.Add 2.Update 3.Display 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_student()

    elif ch == "2":
        update_courses()

    elif ch == "3":
        display()

    elif ch == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!\n")

# Mini Project 10: Number Utility Tool

num = int(input("Enter number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hex:", hex(num))

print("With commas:", f"{num:,}")
print("Scientific:", f"{num:.2e}")