# Проект — electronics-shop-project

Electronics_shop_project — это проект, который представляет собой абстрактный магазин, позволяющий хранить информацию
о товаре, его стоимости и количестве. Также есть возможность получения общей стоимости товаров, добавление товаров из
csv-файла. Данный проект реализован в целях демонстрации владения навыками объектно-ориентированного программирования.
В коде используются библиотеки: `typing`, `csv`, `os`.

# Дополнительная информация

- Файл с товарами находится в директории:
   - `electronics-shop-project/scr/items.csv` </br>
- Модуль `item.py` содержит класс Item. Функционал: </br>
   - Хранение информации о наименовании товара, его стоимости и количестве; </br>
   - Получение общей стоимости товара; </br>
   - Объявление скидки на товар; </br>
   - Добавление товаров из csv-файла. </br>
   - Складывание товаров по атрибуту `quantity`; </br>
- Модуль `keyboard.py` содержит класс Keyboard, унаследованный от Item. Функционал: </br>
   - Унаследованный функционал от класса Item; </br>
   - Изменение языка клавиатуры с `EN` на `RU`, и наоборот. </br>
- Модуль `phone.py` содержит класс Phone, унаследованный от Item. Функционал: </br>
   - Унаследованный функционал от класса Item; </br>
   - Хранение информации о количестве SIM-карт. </br>
- Для просмотра покрытия кода тестами введите в консоли:
   ```
    cd tests
    pytest --cov --cov-report term-missing
    ```

# Клонирование репозитория

В проекте для управления зависимостями используется [poetry](https://python-poetry.org/). </br>
Выполните в консоли: </br>

Для Windows: </br>
```
git clone git@github.com:DmitriiParfenov/electronics-shop-project.git
python -m venv venv
venv\Scripts\activate
pip install poetry
poetry install
```

Для Linux: </br>
```
git clone git@github.com:DmitriiParfenov/electronics-shop-project.git
cd electronics-shop-project
python3 -m venv venv
source venv/bin/activate
curl -sSL https://install.python-poetry.org | python3
poetry install
```