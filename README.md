# phonebook
Телефонная книга на базе встроенной в Python3 Sqlite3.
Базовый функционал:
Поля
  - Имя;
  - Фамилия;
  - Телефон.
 Функции телефонной книмга:
 - Добавление записи.
 - Поиск по всем полям с выводом результатов
 - Удаление записи.
 - Изменение записи.
 
 Имопрт - экспорт.
 Импорт - экспорт данных производится в "леко человеко-читаемые" форматы.
 Это CSV и текст.
 экспорт-импорт производится в следующем порядке полей(слева направо)
 Имя, Фамилмя, телефон. Поле "Фамилия" не может быть пустым.
 Строка заголовков (поля) в файлах импорта/экспорта отсутствует.
 
 для запуска приложения скопировать в один каталог файлы phonebook.py и exim.py.
 Все доп файлы, как то, база дынных, файлы импорта и экспорта будут созадваться в этом каталоге
 Для запуска приложения  - phonebook.py, в нем производится работа с БД : добавление записей,
 поиск, изменение удажение. Удалений всей БД - путем жестокого уничтожения файла phonbook.db.
 exim.py - операции импорта и экспорта.
 
 Базу данных при первом запуске создавать не нужно, генерится самостоятельно.
 
 Импорт данных
 Создаются, согласно правилам файлы в каталоге приложения.
 import_csv.csv или import_txt.txt соотвественно.
!! При импорте в базу данных предыдущие данный удаляются.!!
 
 Экспорт данных
 Искать файлы mport_txt.txt или export_txt.txt в каталоге приложения.
 Дальше использовать по своему усмотрению.
 
Рразработка:
Работа с БД vbifus-spb
Модуль экспорта-импорта - mym2016
 
 
 
 
 
 
 
  
