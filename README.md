# Ближайшие бары

Скрипт рассчитывает:

* самый большой бар;
* самый маленький бар;
* самый близкий бар (пользователю нужно ввести с клавиатуры текущие gps-координаты).

Список московских баров в формате JSON взят с сайта [data.mos.ru](https://data.mos.ru).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py <path_to_your_json_file> # possibly requires call of python3 executive instead of just python
# Пример ответа скрипта
The biggest bar is 
        Name: Спорт бар «Красная машина» 
        Address: Автозаводская улица, дом 23, строение 1
The smallest bar is 
        Name: БАР. СОКИ 
        Address: Дубравная улица, дом 34/29
------------------------------------------------
Enter your latitude: 34
Enter your longitude: 56
The closest bar is 
        Name: Бар «ДЖАНГО» 
        Address: город Зеленоград, корпус 1456

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
