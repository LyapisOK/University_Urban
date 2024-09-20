team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 5
score_1 = 4
score_2 = 5
team1_time = 15
team2_time = 34
challenge_result = ''
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = team1
else:
    challenge_result = team2
tasks_total = score_1 + score_2
time_avg = tasks_total / (team1_time + team2_time)

print('В команде %s участников: %s!' %(team1, team1_num))
print('Итого сегодня в командах участников: %s и %s!' %(team1_num, team2_num))
print('Команда {} решила задач: {}!'.format(team2, score_2))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды {challenge_result}!')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!.')