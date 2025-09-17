# Куди піти? — Django lab

## Запуск
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## Проєкт
- Додаток `places` містить модель Place, список і форму додавання.
- Щоб додати місця для незалогіненого користувача — просто додайте їх (будуть збережені в сесії).
