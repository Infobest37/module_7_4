info1 = ("В команде Мастера кода участников: %(name1)s, %(name2)s, %(name3)s, %(name4)s, %(name5)s! "
      % {"name1": "Денис", "name2": "Евгений", "name3": "Роман", "name4": "Светлана", "name5": "Егор" })
info2 = ("В команде Мастера йода участников: %(name1)s, %(name2)s, %(name3)s, %(name4)s, %(name5)s!, %(name6)s!"
      % {"name1": "Денис", "name2": "Евгений", "name3": "Роман", "name4": "Светлана", "name5": "Егор", "name6": "Юлия" })
print(f"{info1}\n{info2}")
team1_num = 5
team2_num = 6


total_tasks2 = "Команда {comand_name1} решила задач: {tasks} !". format(comand_name1 = "Волшебники данных", tasks = "42")
total_tasks1 = "Команда {comand_name2} решила задач: {tasks} !". format(comand_name2 = "Волшебники данных", tasks = "40")
print(f"{total_tasks1}, {total_tasks2}")
score_1 = 40
score_2 = 42

Total1_time = "{comand_name} решили задачи за {time} с". format(comand_name = "Волшебники данных", time = 18015.2 )
Total2_time = "{comand_name} решили задачи за {time} с". format(comand_name = "Мастера кода", time = 18000.2 )
print(Total1_time,Total2_time)
team1_time = 18015.2
team2_time = 18000.2

f = f"Команды решили {score_1} и {score_2} задач"
print(f)

def result_game():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = "Победа команды Мастера кода!"
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result

print(result_game())



