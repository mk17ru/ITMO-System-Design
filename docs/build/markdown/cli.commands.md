# cli.commands package

## Submodules

## cli.commands.base_command module

Module with Base Command class.

### *class* cli.commands.base_command.BaseCommand(stdin: ~typing.TextIO = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>, stdout: ~typing.TextIO = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

Базовые классы: `ABC`

Base class for all commands.

#### set_args(args: list[Any]) → None

Summary of set_args.

* **Параметры:**
  **args** (*List* *[**Any* *]*) – Description of args.

#### *property* stdin *: TextIO*

Summary of stdin.

* **Результат:**
  Description of return value
* **Тип результата:**
  TextIO

#### *property* stdout *: TextIO*

Summary of stdout.

* **Результат:**
  Description of return value
* **Тип результата:**
  TextIO

## cli.commands.cat_command module

### *class* cli.commands.cat_command.CatCommand(stdin: ~typing.TextIO = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>, stdout: ~typing.TextIO = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

Базовые классы: [`BaseCommand`](#cli.commands.base_command.BaseCommand)

CatCommand logic.

## cli.commands.echo_command module

### *class* cli.commands.echo_command.EchoCommand(stdin: ~typing.TextIO = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>, stdout: ~typing.TextIO = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

Базовые классы: [`BaseCommand`](#cli.commands.base_command.BaseCommand)

EchoCommand logic.

## cli.commands.exit_command module

### *class* cli.commands.exit_command.ExitCommand(stdin: ~typing.TextIO = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>, stdout: ~typing.TextIO = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

Базовые классы: [`BaseCommand`](#cli.commands.base_command.BaseCommand)

ExitCommand logic.

## cli.commands.external_command module

### *class* cli.commands.external_command.ExternalCommand(stdin: ~typing.TextIO = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>, stdout: ~typing.TextIO = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

Базовые классы: [`BaseCommand`](#cli.commands.base_command.BaseCommand)

ExternalCommand logic.

## cli.commands.pwd_command module

### *class* cli.commands.pwd_command.PwdCommand(stdin: ~typing.TextIO = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>, stdout: ~typing.TextIO = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

Базовые классы: [`BaseCommand`](#cli.commands.base_command.BaseCommand)

PwdCommand logic.

## cli.commands.wc_command module

### *class* cli.commands.wc_command.WcCommand(stdin: ~typing.TextIO = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>, stdout: ~typing.TextIO = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

Базовые классы: [`BaseCommand`](#cli.commands.base_command.BaseCommand)

WcCommand logic.

## Module contents
