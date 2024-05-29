# Student Scores API

## Описание

Это упрощенная версия электронного журнала для управления оценками студентов. Приложение предоставляет API для выполнения CRUD операций над студентами и их оценками. 

Технологический стек включает FastAPI, SQLAlchemy и pyyaml, а данные хранятся в базе данных SQLite.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/student-scores-api.git
    cd student-scores-api
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/Mac
    venv\Scripts\activate  # для Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Настройка

1. Убедитесь, что файл `config.yaml` находится в корневом каталоге проекта и настроен правильно. Пример файла `config.yaml`:
    ```yaml
   db:
    dsn: sqlite:///./test.db
    tables:
      students: students
      scores: scores
    ```

2. Проверьте, что путь к базе данных в файле `config.yaml` правильный.

## Запуск

1. Запустите приложение:
    ```bash
    uvicorn app.main:app --reload
    ```

Приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Документация по API

Документация по API доступна по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Примеры использования API

### Студенты

- **Создать нового студента:**
    ```http
    POST /students/
    ```

- **Получить информацию о конкретном студенте:**
    ```http
    GET /students/{student_id}
    ```

- **Обновить информацию о конкретном студенте:**
    ```http
    PATCH /students/{student_id}
    ```

- **Удалить студента:**
    ```http
    DELETE /students/{student_id}
    ```

### Оценки

- **Добавить оценку студенту:**
    ```http
    POST /scores/
    ```

- **Получить информацию о конкретной оценке:**
    ```http
    GET /scores/{score_id}
    ```

- **Обновить информацию о конкретной оценке:**
    ```http
    PATCH /scores/{score_id}
    ```

- **Удалить оценку:**
    ```http
    DELETE /scores/{score_id}
    ```

