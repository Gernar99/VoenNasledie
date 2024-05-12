Устанваливаем python на ПК, после создаем вирутальную среду в проекте с .django (ВСЕ ДЕЙСВТИЯ СОВЕРШАЮТСЯ В ВИРТУАЛЬНОЙ СРЕДЕ):

python -m env env
env\scripts\activate
pip -m install django

Устанавливаем необходимые библиотеки из requirements.txt !!ВНИМАНИЕ!! в файле указана ссылка на один из файлов whl, файл нельзя переименовывать, 
ставиться относительно уставноленного python 
Скачать GDAL и переместить куда хочешь:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#_gdal)

строка выглядит примерно так в requirements.txt GDAL @ file:///C:/Users/dimah/Downloads/GDAL-3.4.3-cp310-cp310-win_amd64.whl
pip install -r requirements.txt

виртуальная среда со всеми библиотеками почти готова, осталось в файле settings.py из mymap изменить пути для GDAL_LIBRARY на тот куда установили вирутальную среду с whl файлом
папка находится внутри виртуальной среды env

GDAL_LIBRARY_PATH = r'C:\Users\dimah\Desktop\gis\venv\Lib\site-packages\osgeo\gdal304.dll'
GEOS_LIBRARY_PATH=r'C:\Users\dimah\Desktop\gis\venv\Lib\site-packages\osgeo\geos_c.dll'
(эти строчки меняем на свои пути)

теперь связываем с PostgreSQL
снова settings.py находим строчку DATABASES меняем под свою, в оригинале БД называется GIS
после связываем библиотеку с PSQL (если интересно, все таблицы описаны в models.py)

в PSQL в указанной БД будут созданы таблицы с указанными типам данных(не работает, скипай)

Восстанавливаем BACKUP по кнопке RESTORE(временно)

заходим в корневую папку проекта и пишем
python manage.py runserver
отобразиться на localhost:8000 или 127.0.0.1:8000 (браузер может хранить временные файлы, поэтому изменения не всегда могут отображаться, проверяйте структуру кода)


Для быстрого запуска, когда запускаешь консоль в корне проекта
venv\scripts\activate
python manage.py runserver
