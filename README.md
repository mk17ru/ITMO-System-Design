# ITMO-System-Design
## Разработка
### Poetry
1) ```poetry env use python3.12```
2) ```poetry install ```
3) Чтобы добавить пакет: ```poetry add <package-name>```

### Pre-commit hooks 
1) ```pre-commit install```
2) При падении, 
поправьте ошибки и вновь сделайте коммит.\
Обратите внимание, что часть ошибок исправляются автоматически.
3) Запустить хуки без коммита на все файлы: ```pre-commit run -a```


## Тестирование
Чтобы запустить тесты вызовите:

```sh
poetry run pytest -vv --showlocals
```

## Документация
1) Docstrings создаются автоматически с помощью пакета [py-doq](https://github.com/heavenshell/py-doq), 
запускаемого прекомитом.\
К сожалению, ```py-doc``` не умеет создавать docstrings для публичных модулей, поэтому необходимо создать их самому
2) С помощью [Sphinx](https://sphinx-ru-ng.readthedocs.io/_/downloads/ru/latest/pdf/), поддерживается пользовательская [Markdown документация](./docs/build/markdown/index.md)

### Sphinx 
Если хотим обновить пользовательскую документацию
1) Для обновления ```source``` файлов ```Sphinx``` в корне проекта запускаем: ```sphinx-apidoc -f -o ./docs/source ./cli```
2) Создание новой версии ```Markdown```: ```cd docs && make markdown```
>>>>>>> cc3e4c4 (small fix)
## Запуск 
### TODO 
