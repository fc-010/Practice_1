marks = [88, 45, 92, 67, 30, 75]

passed = 0
total = 0
highest = marks[0]
lowest = marks[0]

for mark in marks:
    total += mark

    if mark >= 50:
        passed += 1

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total / len(marks)

print(f"Passed: {passed}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}",f"Lowest: {lowest}")