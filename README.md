# Python_Band

Для старта проекта
```
python manage.py makemigrations

python manage.py migrate
```

### Fixtures

Для загрузки фикстур после миграций применить
```
python manage.py loaddata fixtures/fixtures.json
```
В фикстурах добавляется администратор, 4 категории и 12 статей.

Логин администратора admin
Пароль администратора admin