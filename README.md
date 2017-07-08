format.py рекурсивно ищет в текущем и всех вложенных каталогах файлы *.cpp и *.h и форматирует их с помощью clang-format и настроек которые лежат в файле .clang-format. В это же время он проверяет эти файлы на соответствие стилю наименований, который можно настроить через файл format.config. Дефолтные стили тоже есть. Если стили не совпали - пишет в окно тип элемента, его имя, местонахождение (которое выдал силанг) и файл в котором элемент находится. При запуске создается окно, в котором есть одна кнопка - "Begin". Жмем на кнопку и скрипт начинает работу.

В данный момент работает (вроде как) проверка имен неймспейсов, файлов, функций и переменных (в т.ч. констант с отдельным регэкспом).

КАК РАБОТАЕТ format.config:

Пишем название элемента (Namespace, Function, Variable, Filename, Constant), регэксп для которого хотим задать, а потом пишем сам регэксп в следующем формате

Namespace: ^тут мой регэксп*$

Главное условие - регэксп начинается с ^ и заканчивается на $, имя элемента и регэксп находятся на одной строке, во всем остальном файле можно писать что угодно.

ВНИМАНИЕ! Гитхаб не хочется принимать файл без имени, поэтому берем config.txt и переименовываем в .clang-format.  .

Для работы необходимо просто сбросить format.py, format.config и .clang-format в папку с проектом и запустить.

TODO: 

1)Добавить файл в котором можно выбирать расширения файлов

2)Дописать проверку имен классов, тайпдефов, енамов и макросов, просмотреть на баги, получше потестить

3)Переехать с os на subprocess

4)Каким нибудь образом избавиться от силанга, потому что есть одна большая проблема - он начинает все файлы компилировать. Хочется сделать ИДЕ-независимое форматирование, но какой тогда смысл пользоваться силангом, который сначала пытается скомпилить файлы, а уже потом собирает АСТ дерево? Без компиляции он его не строит.

Требуется (условно) рабочий clang-format и питон 3, питон 2 больше не будет работать из-за того, что в третьей версии "Tkinter" заменили на "tkinter". Вероятно будет работать если поменять в коде маленькую t на большую, но я не проверял.

Да, в format.py есть дебажный код, но убирать его я пока не буду.
