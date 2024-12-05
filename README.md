
# Filmoteca API

Filmoteca API — это приложение на Django, предназначенное для управления пользователями, фильмами и избранными фильмами пользователей.

## Функциональность

1. **Пользователи:**
   - Создание нового пользователя.
   - Получение информации о пользователе.
   - Изменение данных пользователя.
   - Удаление пользователя.

2. **Фильмы:**
   - Добавление нового фильма.
   - Получение информации о фильме или списка всех фильмов.
   - Обновление данных о фильме.
   - Удаление фильма.

3. **Избранное:**
   - Добавление фильма в избранное пользователя.
   - Удаление фильма из избранного.
   - Получение списка избранных фильмов для конкретного пользователя.

---

## Установка

### 1. Клонирование репозитория
Склонируйте репозиторий на ваш компьютер:
```bash
git clone git@github.com:AleksandrKosmylev/Indigo.git
cd filmoteca
```

### 2. Создание и активация виртуального окружения


  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### 3. Установка зависимостей
Установите все зависимости, указанные в `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных
Примените миграции для настройки базы данных:
```bash
python manage.py migrate
```

### 5. Создание суперпользователя
Создайте суперпользователя для доступа к административной панели:
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера разработки
Запустите сервер разработки:
```bash
python manage.py runserver
```

Откройте браузер и перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## API Эндпоинты

### Пользователи
- **POST** `/api/users/` — Создание пользователя.
- **GET** `/api/users/<id>/` — Получение информации о пользователе.
- **PUT** `/api/users/<id>/` — Обновление данных пользователя.
- **DELETE** `/api/users/<id>/` — Удаление пользователя.

### Фильмы
- **POST** `/api/movies/films/` — Добавление фильма.
- **GET** `/api/movies/films/` — Получение списка всех фильмов.
- **GET** `/api/movies/films/<id>/` — Получение информации о конкретном фильме.
- **PUT** `/api/movies/films/<id>/` — Обновление данных фильма.
- **DELETE** `/api/movies/films/<id>/` — Удаление фильма.

### Избранное
- **POST** `/api/movies/favorites/` — Добавление фильма в избранное.
  ```json
  {
      "user_id": "user123",
      "film_id": 1
  }
  ```
- **GET** `/api/movies/favorites/?user_id=<user_id>` — Получение списка избранных фильмов пользователя.
- **DELETE** `/api/movies/favorites/<id>/` — Удаление фильма из избранного.

---

## Тестирование

### 1. Использование Postman
- Импортируйте эндпоинты в Postman.
- Выполните запросы к серверу, передавая необходимые параметры.

### 2. Использование Django Browsable API
- Перейдите в браузере по адресу [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).
- Используйте интерфейс для выполнения запросов.
