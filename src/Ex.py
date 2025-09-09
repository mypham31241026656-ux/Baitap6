# Set
# 1.Write a Python program to find the maximum and minimum values in a set.
numbers= {3,4,5,6,24,53,56}
max_value = max(numbers)
min_value = min(numbers)
print("Set elements: ", numbers)
print("Max value: ", max_value)
print("Min value: ", min_value)
# 2.Write a Python program to check if a given value is present in a set or not.
numbers= {3,4,5,6,24,53,56}
value = int(input("Enter a number to check: "))
if value in numbers:
    print("The number is in a set")
else:
    print("The number is not in a set")
# 3.Write a Python program to check if two given sets have no elements in common.
set1 = {3,4,5,6,24,53,56}
set2 = {4,5,2,7,35,94,46}
if set1 - set2 == {}:
    print("Two set have no elements in common")
else:
    print("Two set have elements in common: ", set1 &set2 )
# 4.Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
list = ['He is the man',
        'She is the woman',
        'He is the man',
        'She is the woman']
all_words = []
for line in list:
    words = line.split()
    all_words.extend(words)
unique_words = set(all_words)
print("Unique words and their frequency: ")
for word in unique_words:
    count = all_words.count(word)
    print(f"{word}: {count}")

# 5.Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
#
# Dictionary
# Restructuring the company data: Suppose you have a dictionary that contains information about employees at a company. Each employee is identified by an ID number, and their information includes their name, department, and salary. You want to create a nested dictionary that groups employees by department so that you can easily see the names and salaries of all employees in each department.
#
# Write a Python program that when given a dictionary, employees, outputs a nested dictionary, dept_employees, which groups employees by department.
employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}
dept_employees = {}
for emp_id, info in employees.items():
    dept = info["department"]
    if dept not in dept_employees:
        dept_employees[dept] = {}

    dept_employees[dept][emp_id] = { #thêm nhân viên vào phòng ban (phải nằm trong vòng lặp)
    "name": info["name"],
    "salary": info["salary"],
    }
print("dept_employees = {")
for dept, emps in dept_employees.items():
    print(f"{dept}: {{")
    for emp_id, data in emps.items():
        print(f' {emp_id}: {data},')
    print('},')
print("}")
