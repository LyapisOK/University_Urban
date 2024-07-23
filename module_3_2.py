def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    Domains = ['.com', '.ru', '.net']
    simb = '@'
    if simb not in recipient or simb not in sender or (recipient[-4:] not in Domains and recipient[-3:] not in Domains) or (sender[-4:] not in Domains and sender[-3:] not in Domains):
        answer = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    elif recipient == sender:
        answer = f'Нельзя отправить письмо самому себе!'
    elif sender == 'university.help@gmail.com':
        answer = f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.'
    else:
        answer = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.'
    return answer

text = send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print(text)
text = send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print(text)
text = send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print(text)
text = send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print(text)
