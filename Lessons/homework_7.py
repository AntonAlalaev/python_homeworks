grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Сначала сделаем список
students = list(students)
# Отсортируем его по алфавиту
students.sort()
print(students)
res = {}
for i in range(0, len(students)):
    key = students[i]
    value = sum(grades[i])/(len(grades[i]))
    res[key] = value
print(res)
