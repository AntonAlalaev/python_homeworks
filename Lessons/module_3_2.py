# Функция проверяет email адреса на корректность
def check_email(email):
    if not ("@" in email):
        return False
    domain = False
    if ".net" in str.lower(email):
        domain = True
    if ".ru" in str.lower(email):
        domain = True
    if ".com"  in str.lower(email):
        domain = True
    return domain

# Функция сравнивает email адреса
def compare_str(string1, string2):
    if str.lower(string1) == str.lower(string2):
        return True
    return False

# Функция отправки e-mail
def send_email(message, recipient, sender = "university.help@gmail.com"):
    # Проверка на корректность адресов email
    if not (check_email(recipient) and check_email(sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return False
    if compare_str(recipient,sender):
        print(f"Нельзя отправить сообщение самому себе! Адреса отправителя и получателя совпадают")
        return False
    if str.lower(sender) != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! ")
    print(f"Письмо успешно отправлено с адреса {sender}, на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')