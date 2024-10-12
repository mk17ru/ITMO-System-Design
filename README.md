# ITMO-System-Design
## Разработка
### Poetry
1) ```poetry env use python3.12```
2) ```poetry install ```
3) Чтобы добавить пакет: ```poetry add <package-name>```
### Pre-commit hooks 
1) ```pre-commit install```
2) При падении какого-либо хука, 
поправьте ошибки и вновь сделайте коммит.\
Обратите внимание, что часть ошибок исправляются автоматически.


## Тестирование
Чтобы запустить тесты вызовите:

```sh
poetry run pytest -vv --showlocals
```

## Запуск 
### TODO 
