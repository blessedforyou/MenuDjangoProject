# Django Menu Project

## 📖 Описание

**MenuDjangoProject** — это тестовый проект на Django, который реализует древовидное меню с использованием шаблонных тегов. Проект демонстрирует, как создать меню с подменю, хранимое в базе данных, с возможностью редактирования через стандартную админку Django. Меню поддерживает работу с URL, как явными, так и именованными, и отображает активный пункт меню на основе текущего URL.

### Основные возможности
- 🌳 Древовидное меню с поддержкой дополнительных подменю.
- 🛠️ Меню и подменю хранятся в базе данных и редактируются через стандартную админку Django.
- 🌐 Поддержка явных и именованных URL.
- 🔍 Определение активного пункта меню на основе текущего URL.

## 🚀 Установка и запуск проекта

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/blessedforyou/MenuDjangoProject.git
    ```

2. Перейдите в папку проекта:

    ```bash
    cd MenuDjangoProject
    ```

3. Создайте и активируйте виртуальное окружение:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

4. Примените миграции:

    ```bash
    python manage.py migrate
    ```

5. Создайте суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

## 📚 Использование

1. **Создание основного меню** в админке.
2. **Добавление подменю**, указав связь с основным меню.
3. **Прямой URL** — берётся из `urls.py` (например, `/services/`).
4. **Именованный URL** — также берётся из `urls.py` (например, `services`). Для работы именованный URL должен быть создан заранее.
5. **Использование в шаблоне**: передайте в `base.html` -> `{% draw_menu 'slug' %}` слаг из основного меню.

### Примеры использования

- **Menu -> Product (Title) -> product (slug)**
- **Menu -> News (Title) -> /product/news/ (URL) -> Product (Menu)**
- **Menu -> News (Title) -> new-product (named URL) -> Product (Menu)**

В шаблоне `base.html`:
```django
{% load 'product' %}
