# ==========================================
# ADVANCED TO-DO LIST MANAGER
# PYTHON LISTS PROJECT
# ==========================================

# 1. CREATING A NESTED LIST

tasks = [
    ["Study Python", "High", 60, "Pending"],
    ["Exercise", "Medium", 30, "Completed"],
    ["Complete homework", "High", 45, "Pending"],
    ["Read book", "Low", 20, "Completed"]
]

# Each inner list:
# [Task Name, Priority, Duration, Status]


print("\n========== MY TO-DO LIST ==========")


# 2. DISPLAYING TASKS USING enumerate()

for index, task in enumerate(tasks, start=1):
    print(
        index, task[0], "|",
        task[1], "|",
        task[2], "min |",
        task[3]
    )


# 3. INDEXING AND NEGATIVE INDEXING

print("\n========== INDEXING ==========")

print("First task:", tasks[0])
print("First task name:", tasks[0][0])
print("Last task:", tasks[-1])
print("Last task name:", tasks[-1][0])


# 4. LIST SLICING

print("\n========== SLICING ==========")

print("First two tasks:", tasks[:2])
print("Last two tasks:", tasks[-2:])
print("Reverse list:", tasks[::-1])


# 5. UPDATING LIST ELEMENTS

print("\n========== UPDATING ==========")

tasks[0][0] = "Learn Python Programming"

print("Updated first task:", tasks[0])

# Slice assignment example
sample_tasks = ["Study", "Exercise", "Read", "Sleep"]

sample_tasks[0:2] = ["Coding", "Walking"]

print("After slice assignment:", sample_tasks)


# 6. APPEND, INSERT AND EXTEND

print("\n========== ADDING TASKS ==========")

tasks.append(["Practice coding", "High", 40, "Pending"])

tasks.insert(
    1,
    ["Attend class", "Medium", 50, "Pending"]
)

tasks.extend([
    ["Revise strings", "Low", 25, "Pending"],
    ["Upload project", "High", 15, "Pending"]
])

print("After adding tasks:")

for task in tasks:
    print(task)


# 7. REMOVE, POP AND DEL

print("\n========== REMOVING TASKS ==========")

sample = ["Study", "Exercise", "Reading", "Shopping"]

sample.remove("Exercise")
print("After remove:", sample)

removed_task = sample.pop(1)
print("Popped task:", removed_task)
print("After pop:", sample)

del sample[-1]
print("After del:", sample)


# 8. CLEAR METHOD

temporary_tasks = ["Task 1", "Task 2"]

temporary_tasks.clear()

print("After clear:", temporary_tasks)


# 9. SEARCHING AND COUNTING

print("\n========== SEARCHING ==========")

task_names = [task[0] for task in tasks]

print("Task position:", task_names.index("Read book"))
print("Task count:", task_names.count("Read book"))

print("Is Study Python present?", "Study Python" in task_names)
print("Is Shopping absent?", "Shopping" not in task_names)


# 10. SORTING LISTS

print("\n========== SORTING ==========")

numbers = [40, 10, 30, 20]

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

numbers.reverse()
print("Reversed:", numbers)

sorted_copy = sorted(numbers)
print("Sorted copy:", sorted_copy)
print("Original list:", numbers)


# 11. SORTING TASKS USING key

print("\n========== SORTING TASK NAMES ==========")

task_names.sort(key=len)

print("Sorted by name length:", task_names)

task_names.sort(key=len, reverse=True)

print("Longest names first:", task_names)


# 12. LIST COPYING

print("\n========== LIST COPYING ==========")

original = [10, 20, 30]

assigned = original
shallow_copy = original.copy()
slicing_copy = original[:]

original.append(40)

print("Original:", original)
print("Assignment:", assigned)
print("Copy method:", shallow_copy)
print("Slicing copy:", slicing_copy)


# Deep copy of nested lists
nested_original = [["Study", 60], ["Exercise", 30]]

from copy import deepcopy

deep_copy = deepcopy(nested_original)

nested_original[0][0] = "Coding"

print("Nested original:", nested_original)
print("Deep copy:", deep_copy)


# 13. LIST OPERATORS

print("\n========== LIST OPERATORS ==========")

list1 = ["Study", "Exercise"]
list2 = ["Reading", "Coding"]

print("Combined:", list1 + list2)
print("Repeated:", list1 * 2)

print("Study exists:", "Study" in list1)
print("Shopping absent:", "Shopping" not in list1)


# 14. LIST UNPACKING

print("\n========== LIST UNPACKING ==========")

subjects = ["Python", "Maths", "English"]

subject1, subject2, subject3 = subjects

print(subject1)
print(subject2)
print(subject3)


# 15. LIST COMPREHENSION

print("\n========== LIST COMPREHENSION ==========")

all_tasks = [
    "Study Python",
    "Exercise",
    "Complete homework",
    "Practice coding",
    "Read book"
]

# Normal list comprehension
study_tasks = [
    task for task in all_tasks
    if "Study" in task or "Practice" in task
]

print("Selected tasks:", study_tasks)


# 16. LIST COMPREHENSION WITH IF-ELSE

task_status = [
    "Learning Task" if "Study" in task or "Practice" in task
    else "Other Task"
    for task in all_tasks
]

print("Task labels:", task_status)


# 17. BUILT-IN LIST FUNCTIONS

print("\n========== LIST STATISTICS ==========")

durations = [25, 40, 60, 15, 30]

completed = [True, True, False, True, False]

print("Number of tasks:", len(durations))
print("Total duration:", sum(durations))
print("Shortest task:", min(durations))
print("Longest task:", max(durations))
print("At least one completed:", any(completed))
print("All completed:", all(completed))


# 18. ENUMERATE

print("\n========== ENUMERATE ==========")

for index, task in enumerate(all_tasks, start=1):
    print(index, task)


# 19. ZIP

print("\n========== ZIP ==========")

statuses = ["Pending", "Completed", "Pending", "Pending", "Completed"]

for task, status in zip(all_tasks, statuses):
    print(task, "-", status)


# 20. ITERATING THROUGH LISTS

print("\n========== FOR LOOP ==========")

for task in all_tasks:
    print(task)


print("\n========== RANGE LOOP ==========")

for i in range(len(all_tasks)):
    print(all_tasks[i])


print("\n========== WHILE LOOP ==========")

i = 0

while i < len(all_tasks):
    print(all_tasks[i])
    i += 1


# 21. MUTABILITY

print("\n========== MUTABILITY ==========")

mutable_tasks = ["Study", "Exercise"]

mutable_tasks[0] = "Learn Python"

print("Changed list:", mutable_tasks)


print("\n========== PROJECT COMPLETED ==========")
