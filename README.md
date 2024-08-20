**Django Menu Project**

**Описание**

MenuDjangoProject — это тестовый проект на Django, который реализует древовидное меню с использованием шаблонных тегов. Проект демонстрирует, как создать меню с подменю, хранимое в базе данных, с возможностью редактирования через стандартную админку Django. Меню поддерживает работу с URL, как явными, так и именованными, и отображает активный пункт меню на основе текущего URL.

**Основные моменты**

- Древовидное меню с поддержкой доп.меню
- Меню и доп.меню хранятся в БД и редактируются через админку Django
- Поддержка явных и именованных URL
- Активный пункт определяется на основе текущего URL

**Установка и запуск проекта**

git clone https://github.com/blessedforyou/MenuDjangoProject.git
cd MenuDjangoProject
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


**Использование**

- Создание основного меню в админке.
- Добавление доп. меню, указав связь с основ. меню.
- Прямой URL - берется из urls.py (/services/)
- Именованный URL - берется также из urls.py (services) (Для работы он должен быть создан заранее)
- Передача в base.html -> {% draw_menu 'slug' %} слага из основного меню.

**Пример**
Menu -> Product (Title) -> product (slug)
Menu -> News (Title) -> /product/news/ (URL) -> Product (Menu) or Menu -> News (Title) -> new-product (named URL) -> Product (Menu)
base.html -> {% load 'product' %} (slug)
