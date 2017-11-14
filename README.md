# Ближайшие бары

Скрипт рассчитывает:

* самый большой бар;
* самый маленький бар;
* самый близкий бар (пользователю нужно ввести с клавиатуры текущие gps-координаты).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py <path_to_your_json_file> # possibly requires call of python3 executive instead of just python
# Пример ответа скрипта
The biggest bar is: Спорт бар «Красная машина»
The smallest bar is: Бар в Деловом центре Яуза
--------------------------------------
Enter your longitude: 12
Enter your latitude: 12
Staropramen is closest bar to you.

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
