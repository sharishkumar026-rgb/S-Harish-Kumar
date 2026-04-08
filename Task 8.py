import mysql.connector
from functools import reduce
from abc import ABC, abstractmethod

#  Database Connection
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Harish@12345",
    database="expense_db"
)

print(" Connected to MySQL")

cursor = conn.cursor()


#  Abstract Class
class ExpenseBaseManager(ABC):

    @abstractmethod
    def view_expenses(self):
        pass


#  User Class
class User:
    def __init__(self, name):
        self.__name = name

    def add_user(self):
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (self.__name,))
        conn.commit()
        print("User added")


# Expense Class (MAIN CLASS)
class Expense(ExpenseBaseManager):

    def __init__(self, user_id):
        self.__user_id = user_id

    def add_expense(self, amount, category, description, date):
        query = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (self.__user_id, amount, category, description, date))
        conn.commit()
        print(" Expense added")

    # ✔ Required (Abstract method implemented)
    def view_expenses(self):
        query = """
        SELECT u.name, e.amount, e.category, e.description, e.date
        FROM users u
        JOIN expenses e ON u.user_id = e.user_id
        WHERE u.user_id = %s
        """
        cursor.execute(query, (self.__user_id,))
        data = cursor.fetchall()

        print("\n Expenses:")
        for row in data:
            print(row)

        return data

    def filter_expenses(self, data, category=None, date=None):
        if category:
            data = list(filter(lambda x: x[2] == category, data))
        if date:
            data = [d for d in data if str(d[4]) == date]
        return data

    def total_expense(self, data):
        amounts = list(map(lambda x: x[1], data))
        return reduce(lambda a, b: a + b, amounts, 0)

    def category_spending(self, data):
        result = {}
        for d in data:
            result[d[2]] = result.get(d[2], 0) + d[1]
        return result

    def monthly_report(self, data):
        report = {}
        for d in data:
            month = str(d[4])[:7]
            report[month] = report.get(month, 0) + d[1]
        return report

    def highest_expense(self, data):
        if not data:
            return "No data"
        return reduce(lambda a, b: a if a[1] > b[1] else b, data)

    def smart_insight(self, data):
        if not data:
            return "No data"
        cat = self.category_spending(data)
        return f"You are spending too much on {max(cat, key=cat.get)}"


# MAIN

#  Create user (run once)
# user = User("Harish")
# user.add_user()

exp = Expense(user_id=1)

#  Add expense (run once if no data)
# exp.add_expense(500, "Food", "Lunch", "2026-04-08")

data = exp.view_expenses()
print("DEBUG:", data)

if not data:
    print(" No data found!")
else:
    print("Total:", exp.total_expense(data))
    print("Category:", exp.category_spending(data))
    print("Monthly:", exp.monthly_report(data))
    print("Highest:", exp.highest_expense(data))
    print("Insight:", exp.smart_insight(data))


conn.close()