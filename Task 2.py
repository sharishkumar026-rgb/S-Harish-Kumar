
# BITWISE OPERATORS (1–8)

# 1
a = 10
b = 6
print("1:", a & b)

# 2
x = 12
y = 5
print("2:", x | y)

# 3
num = 8
print("3:", ~num)

# 4
a = 15
b = 9
print("4:", a ^ b)

# 5
num = 7
print("5:", num << 2)

# 6
num = 20
print("6:", num >> 1)

# 7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("7:", a & b)

# 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("8:", a ^ b)

# STRING TASKS (9–14)

# 9
print("9:", "hi" * 4)

# 10
print("10:", "python" * 3)

# 11
print("11:", "super" + "man")

# 12
print("12:", "hello" + " " + "world")

# 13
name = input("Enter your name: ")
print("13:", name * 5)

# 14
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("14:", s1 + s2)

# INPUT & TYPE CASTING (15–20)

# 15
name = input("Enter name: ")
print("15:", type(name))

# 16
age = int(input("Enter age: "))
print("16:", age)

# 17
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("17:", a + b)

# 18
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
print("18:", (m1 + m2) / 2)

# 19
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("19:", 3*a*2 + b - 2)

# 20
num = input("Enter number: ")
print("Before:", type(num))
num = int(num)
print("After:", type(num))

# UNIT DIGIT (21–25)

# 21
num = input("Enter number: ")
print("21:", num[-1])

# 22
num = int(input("Enter number: "))
print("22:", num % 10)

# 23
num = int(input("Enter number: "))
print("23:", num // 10)

# 24
num = int(input("Enter number: "))
print("24:", (num // 10) % 10)

# 25
num = int(input("Enter 5-digit number: "))
print("25:", num % 10)

# IF STATEMENT (26–30)

# 26
if 10 >= 5:
    print("26: 10 is greater than or equal to 5")

# 27
num = int(input("Enter number: "))
if num > 50:
    print("27: Greater than 50")

# 28
age = int(input("Enter age: "))
if age >= 18:
    print("28: Eligible")

# 29
num = int(input("Enter number: "))
if num > 100:
    print("29: Greater than 100")

# 30
num = int(input("Enter number: "))
if num >= 0:
    print("30: Non-negative")

# IF-ELSE (31–34)

# 31
num = int(input("Enter number: "))
if num % 2 == 0:
    print("31: Even")
else:
    print("31: Odd")

# 32
marks = int(input("Enter marks: "))
if marks >= 35:
    print("32: Pass")
else:
    print("32: Fail")

# 33
num = int(input("Enter number: "))
if num >= 0:
    print("33: Positive")
else:
    print("33: Negative")

# 34
num = int(input("Enter number: "))
if num > 10:
    print("34: Greater than 10")
else:
    print("34: Not greater than 10")


# NESTED IF (35–37)

# 35
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("35: Selected")
        else:
            print("35: Rejected (weight)")
    else:
        print("35: Rejected (height)")
else:
    print("35: Rejected (age)")

# 36
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("36: Admission Granted")
    else:
        print("36: Age not eligible")
else:
    print("36: Marks not eligible")

# 37
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("37: Selected")
        else:
            print("37: Rejected (weight)")
    else:
        print("37: Rejected (height)")
else:
    print("37: Rejected (age)")

# MATCH CASE (38–40)

# 38
day = int(input("Enter day number (1-7): "))
match day:
    case 1: print("38: Monday")
    case 2: print("38: Tuesday")
    case 3: print("38: Wednesday")
    case 4: print("38: Thursday")
    case 5: print("38: Friday")
    case 6: print("38: Saturday")
    case 7: print("38: Sunday")
    case _: print("38: Invalid")

# 39
color = int(input("Enter number (1-3): "))
match color:
    case 1: print("39: Red")
    case 2: print("39: Blue")
    case 3: print("39: Green")
    case _: print("39: Invalid")

# 40
fruit = int(input("Enter number (1-4): "))
match fruit:
    case 1: print("40: Apple")
    case 2: print("40: Mango")
    case 3: print("40: Orange")
    case 4: print("40: Banana")
    case _: print("40: Invalid")
