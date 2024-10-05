team1_num = 5 # Количество участников в первой команде
team2_num = 6 # Количество участников во второй команде

team1_name = "Мастера кода" # название первой команды
team2_name = "Волшебники данных" # название второй команды

team1_score = 40
team2_score = 42

team1_time = 18015.2
team2_time = 19020.2

# Использование %s
print("В команде %s участников: %s" % (team1_name, team1_num))
print("В команде %(name)s участников: %(num)s" % {"name": team2_name, "num": team2_num})
print("Итого сегодня в командах участников: %s и %s" % (team1_num, team2_num))



# Использование format
print("Команда {} решила задач: {}".format(team1_name, team1_score))
print("Команда {} решила задач: {}".format(team2_name, team2_score))
print("{} решили задачи за {} c.".format(team1_name, team1_time))
print("{} решили задачи за {} c.".format(team2_name, team2_time))

# f-строки
print(f"Команды решили {team1_score} и {team2_score} задач.")

if team1_score > team2_score or (team1_score == team2_score and team1_time > team2_time):
    challenge_result = f"Победила команда {team1_name}"
elif team1_score  < team2_score  or (team1_score == team2_score  and team1_time < team2_time):
    challenge_result = f"Победила команда {team2_name}"
else:
    challenge_result = "Ничья"
print(f"Результат соревнования: {challenge_result}")

print(f"В общей сложности команды решили {team1_score + team2_score} задач.")
print(f"Среднее время решения {round((team1_time+team2_time)/(team1_score + team2_score),2)} секунды на задчу.")
