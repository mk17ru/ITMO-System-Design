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
запускаемого прекомитом.
К сожалению, ```py-doc``` не умеет создавать docstrings для публичных модулей, поэтому необходимо создать их самому
2) Sphinx 
## Запуск 
### TODO 
