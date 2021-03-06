



# DataLakePlan (Model DATA VAULT of Dan Linstedt or ANCHOR MODELING of Lars Ronnback)
Python library for Data Lake (model: data vault or data vault A) visualization using excel (it will be a real wall paper of A4 sheets)

README: http://www.anchormodeling.com/

Just try it:

conda install -c musicnova datalakeplan

OR

pip install datalakeplan

[RU/EN]

Идея в следующем.

1. Из Jupyter запускаем команду создать проект.
Появляется каталог с файлами 01_document.xls и 01_example.xls.
Файлы одинаковые практически, только draft пустой, а в example есть пара примеров.

В файлах 5 листов (изменения, описание, таблицы, аттрибуты, примеры).
Пользователь их заполняет по своим источникам и сохраняет готовый файл в 01_document.xls.

2. Из Jupyter запускаем команду создать схему data vault.
В каталоге появится файл 02_schema.xls и 02_sample.xls.
Файлы одинаковые практически, только schema пустой, а в example есть пара примеров.

В нем новые вкладки: hubs, links for hubs, links for links, links for links for links, sattelites, mappings, etl 0, etl 1, etl 2, etl 3, etl 4.

Пользователь их заполняет по минимуму хотя бы hubs и сохраняет готовый файл в 02_schema.xls.

[Идея на подумать - для 4-5 типов баз данных MSSQL, Oracle, Vertica, PostgreSQL, Hive сделать в шаблоне заготовку SQL создания таблицы, view и Python скрипта формулой, чтобы можно было в Excel продублировать запись и не писать скрипты, а генерировать]
[Идея#2 на подумать - закладки Excel задать с буквами A1.Hubs, A2.Hubs, B1.Links, B2.Links, C1.Sattelites, C2.Sattelites]
[Идея#3 на подумать - сгенерировать лист D1.Versions с CRC32 суммой по именам таблиц Links+Hubs, окружающих данную, потом уменьшить количество цифр до 4 с помощью группировки по 8 цифр и взятия остатка от деления на 10 (аналогично для Links+Hubs+Sattelites) и такую h012345678 дописать к таблицам как суффикс, либо на закладке генерировать v201801011030 с соответствием этим двум crc32]

3. Из Jupyter запускаем команду создать карту data lake.
В каталоге появится файл 03_lake.xls и 03_dummy.xls.
Файлы одинаковые практически, только dummy пустой или с примерами, а в lake подготовленная визуализация.

В нем новые вкладки: lake

Пользователь их комментирует и меняет по минимуму и сохраняет готовый файл в 03_lake.xls.

Алгоритм авто построения следующий - решается задача о расположении графа на плоскости.
Параметрами заданы размеры узловых кругов и фиксированное расстояние.

Размер таблицы задает прямоугольник, вокруг которого мы описываем окружность.
Эту окружность мы заменим на цепочку узловых кругов (вписанный n угольник).

Остальные связи подбираем по верхней левой точке таблицы без учета какой fk куда приходит.
Получаем решение об оптимальном расположении графа на плоскости.

Убираем связи между таблицами и рисуем их заново по всем fk.
Желательно для этого продумать внутренний формат хранения вида yaml.

Теперь все стрелки под углом мы заменяем на excel формат оформления границ (например, только сверху или сверху и справа).
Стрелку делим на 4 ступеньки примерно в равных пропорциях, но стараемся, чтобы не пересекались разные стрелки более чем в одной ячейке.

В итоге таблицы делим по префиксам H_ - квадрат, S_ - круг, L - ромб и тоже оформляем выделениями, нумеруем N0001.t1, N00002.t2 и т д. Прорисовываем над H_ и S_ view (обводка с отступом в 2 ячейки), также делаем для L_ и S_ или L_ и L_ и S_ и S_.
Дополнительно находим границы листов A4 и отмечаем в нижнем правом углу буквами координаты, например E1.
(Не забыть, что у всех кроме H_ есть fromDate, toDate и loadDtTm для партиционирования).
(Не забыть, что у H_ есть business key _bk и load_date и source_sys).

Сверху могут быть изображены источники как A1U44, A2U31,... используемые и B1U7, B2U6, ... неиспльзуемые.
У аттрибутов в префиксе указывается "(fk) ", если это foreign key и в суффиксе указывается "[A1U44, A2U31, ...]" все ссылки на источники. Здесь U - это пользовательская нумерация из 01_document.xls.

[Идея на подумать - если связи между таблицами тоже разбить в последовательные цепочки из 4-х элементов, то потом стрелки в excel будет нарисовать сильно проще]
[BAD Идея#2 на подумать - если в N угольник таблицы добавить K элементов (по количеству Foreign Keys) и зарисовать стрелки последовательными цепочками из 4-х элементов, то потом может быть сильно проще распутать эти связи]

4. Из Jupyter запускаем команду создать бумагу data paper.
В каталоге появится файл 04_paper.xls и 04_empty.xls.
Файлы одинаковые практически, только empty пустой или с примерами, а в paper подготовленные обои.

В нем новые вкладки: N00001.A1, N000002.A2, ... N000064.E2
Их можно отправить на печать и получить обои на стену.

Алгоритм должен не посто скопировать ячейки из файла 03_lake.xls в 04_paper.xls, но и разнести по ячейкам длинный текст (расчет ширины букв).

Вот как-то так.
Успехов в работе!




https://www.codementor.io/arpitbhayani/host-your-python-package-using-github-on-pypi-du107t7ku ﻿

STEP1 READ https://www.codementor.io/arpitbhayani/host-your-python-package-using-github-on-pypi-du107t7ku https://stackoverflow.com/a/45209514
STEP2 READ https://pep8.ru/doc/tutorial-3.1/6.html
STEP3 READ https://docs.python.org/3/distutils/configfile.htmlhttps://stackoverflow.com/a/27093036
STEP4 READ https://openpyxl.readthedocs.io/en/stable/
hg clone https://bitbucket.org/openpyxl/openpyxl

hg up 2.5

virtualenv openpyxl

cd openpyxl

source bin/activate

pip install -U -r requirements.txt

python setup.py develop

py.test --cov openpyxl/cell openpyxl/cell

tox -e doc

STEP5 READ https://conda.io/docs/user-guide/tutorials/build-pkgs.html
STEP6 READ https://conda.io/docs/commands/build/conda-develop.html

