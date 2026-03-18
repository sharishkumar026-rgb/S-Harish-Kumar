# Loop Basics (1-10)

# 1. Print numbers 1 to 50
for i in range(1, 51):
    print(i)

# 2. Even numbers 1 to 100
for i in range(2, 101, 2):
    print(i)

# 3. Odd numbers 1 to 100
for i in range(1, 101, 2):
    print(i)

# 4. Table of 7
for i in range(1, 11):
    print(7 * i)

# 5. Sum 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)

# 6. Reverse 50 to 1
for i in range(50, 0, -1):
    print(i)

# 7. Count divisible by 3
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(count)

# 8. Squares 1 to 10
for i in range(1, 11):
    print(i**2)

# 9. Cubes 1 to 10
for i in range(1, 11):
    print(i**3)

# 10. Input n
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i)

# While Loop (11–15)

# 11. 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1

# 12. Factorial
n = int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# 13. Reverse number
num = int(input("Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)

# 14. Count digits
num = int(input("Enter number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(count)

# 15. Until "stop"
while True:
    user = input("Enter something: ")
    if user == "stop":
        break

# Nested Loop (16–20)

# 16. *
for i in range(1, 5):
    print("*" * i)

# 17. 1, 12, 123...
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18. Table 1 to 5
for i in range(1, 6):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()

# 19. A B C
for i in range(3):
    for j in ['A', 'B', 'C']:
        print(j, end=" ")
    print()

# 20. Matrix
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

# String Basics (21–25)

s = input("Enter string: ")

# 21. Count characters
print(len(s))

# 22. Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

# 23. Count consonants
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1
print(count)

# 24. Reverse string
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# 25. Palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# String Slicing (26–30)
# 26
print(s[:5])

# 27
print(s[-3:])

# 28
print(s[::-1])

# 29
print(s[::2])

# 30
print(s[1:-1])

# List Basics (31–35)

lst = [1, 2, 3, 4, 5]

# 31. Sum
print(sum(lst))

# 32. Max
print(max(lst))

# 33. Min
print(min(lst))

# 34. Count elements
print(len(lst))

# 35. Check element
x = int(input("Enter element: "))
if x in lst:
    print("Exists")
else:
    print("Not Exists")

# List Operations (36–40)

lst = []

# 36. Append
lst.append(10)
lst.append(20)
lst.append(30)

# 37. Insert
lst.insert(1, 15)

# 38. Remove
lst.remove(20)

# 39. Reverse without reverse()
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print(rev)

# 40. Sort without sort()
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)
                 