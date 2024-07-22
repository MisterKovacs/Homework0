def send_email(message, recipient, sender = "university.help@gmail.com"):
    suffix = ('.ru', '.com', '.net')
    if '@' not in recipient or not recipient.endswith(suffix):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '@' not in sender or not sender.endswith(suffix):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif 'university.help@gmail.com' == sender:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Hello!', 'ural4eg@gmail.uk')
send_email('Hello!', 'university.help@gmail.com')
send_email('Hello!','ural4eg@gmail.com')
send_email('Hello!', 'ural4eg@gmail.com', 'urban.fan@mail.ru')