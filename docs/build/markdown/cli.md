# cli package

## Subpackages

* [cli.commands package](cli.commands.md)
  * [Submodules](cli.commands.md#submodules)
  * [cli.commands.base_command module](cli.commands.md#module-cli.commands.base_command)
    * [`BaseCommand`](cli.commands.md#cli.commands.base_command.BaseCommand)
      * [`BaseCommand.set_args()`](cli.commands.md#cli.commands.base_command.BaseCommand.set_args)
      * [`BaseCommand.stdin`](cli.commands.md#cli.commands.base_command.BaseCommand.stdin)
      * [`BaseCommand.stdout`](cli.commands.md#cli.commands.base_command.BaseCommand.stdout)
  * [cli.commands.cat_command module](cli.commands.md#module-cli.commands.cat_command)
    * [`CatCommand`](cli.commands.md#cli.commands.cat_command.CatCommand)
  * [cli.commands.echo_command module](cli.commands.md#module-cli.commands.echo_command)
    * [`EchoCommand`](cli.commands.md#cli.commands.echo_command.EchoCommand)
  * [cli.commands.exit_command module](cli.commands.md#module-cli.commands.exit_command)
    * [`ExitCommand`](cli.commands.md#cli.commands.exit_command.ExitCommand)
  * [cli.commands.external_command module](cli.commands.md#module-cli.commands.external_command)
    * [`ExternalCommand`](cli.commands.md#cli.commands.external_command.ExternalCommand)
  * [cli.commands.pwd_command module](cli.commands.md#module-cli.commands.pwd_command)
    * [`PwdCommand`](cli.commands.md#cli.commands.pwd_command.PwdCommand)
  * [cli.commands.wc_command module](cli.commands.md#module-cli.commands.wc_command)
    * [`WcCommand`](cli.commands.md#cli.commands.wc_command.WcCommand)
  * [Module contents](cli.commands.md#module-cli.commands)

## Submodules

## cli.executor module

### *class* cli.executor.Executor

Базовые классы: `object`

Executor logic.

#### *static* execute(parsed_commands: list[[BaseCommand](cli.commands.md#cli.commands.base_command.BaseCommand)]) → int

Summary of execute.

* **Параметры:**
  **parsed_commands** (*list* *[*[*base_command.BaseCommand*](cli.commands.md#cli.commands.base_command.BaseCommand) *]*) – List of parsed_commands.
* **Результат:**
  Status code
* **Тип результата:**
  int

#### output_data *: str* *= '123'*

## cli.parser module

### *class* cli.parser.Parser

Базовые классы: `object`

Parser logic.

#### *static* parse(text: str) → list[[BaseCommand](cli.commands.md#cli.commands.base_command.BaseCommand)]

Summary of parse.

* **Параметры:**
  **text** (*str*) – Description of text.
* **Результат:**
  Description of return value
* **Тип результата:**
  *List*[[base_command.BaseCommand](cli.commands.md#cli.commands.base_command.BaseCommand)]

## cli.presenter module

Presenter component module.

### *class* cli.presenter.Presenter(output_stream: ~typing.TextIO = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

Базовые классы: `object`

Presenter logic.

#### show(data: str) → None

Summary of show.

* **Параметры:**
  **data** (*str*) – Description of data.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

## cli.reader module

### *class* cli.reader.Reader

Базовые классы: `object`

Reader logic.

#### *static* read(input_stream: ~typing.TextIO = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>) → str

Reads strings from the input stream.

## cli.storage module

### *class* cli.storage.Storage

Базовые классы: `object`

Storage logic.

#### get(key: str) → Any

Gets the value associated with the key from the storage.

Returns None if the key is not present.

#### set(key: str, val: Any) → None

Adds a key-value pair to the storage.

## Module contents
