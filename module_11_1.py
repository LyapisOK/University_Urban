"""Для решения задачи я выбрал библиотеки requests, pandas и matplotlib."""
import requests # подключаем библиотеку requsts
import pandas as pd # подключаем библиотеку pandas и даем имя pd
import matplotlib.pyplot as plt # подключаем библиотеку matplotlib и даем имя plt
import math # подключаем библиотеку math

url = 'https://api.github.com/users/LyapisOK' # присваиваем переменной url адрес страницы на Git

"""отправляем GET-запрос на API GitHub и получаем данные о пользователе"""

response = requests.get(url)
data = response.json()

""" Выводим имя пользователя и дату регистрации"""

print(f'Имя пользователя: {data["name"]} \nДата регистрации на Git: {data["created_at"]}')
"""-----------------------"""
"""В этом примере мы создаём DataFrame с данными о трёх людях. Затем мы вычисляем их средний возраст и балл."""
data = {
    'Name': ['Sasha', 'Kolya', 'Nina'],
    'Age': [25, 30, 35],
    'Score': [80, 90, 70]
}

df = pd.DataFrame(data)

# Вычисляем средний балл
average_age = df['Age'].mean()
average_score = df['Score'].mean()
print(f'Средний возраст - {average_age}\nСредний балл - {average_score}')
"""-----------------------"""
"""В этом примере мы создаем график, на котором по оси X отложены значения x, а по оси Y — значения y. Затем мы добавляем заголовок, метки и показываем график."""
x = []
y = []
for i in range(-10, 11):
    x.append(i)
    y.append(math.sin(i))
plt.plot(x, y)
plt.title('График функции Y=sinX')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()