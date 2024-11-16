import os

import cli.commands.base_command as base_command


class LsCommand(base_command.BaseCommand):
    """Логика для команды `ls`."""

    def __call__(self) -> int:
        """Выполнение команды `ls` для отображения содержимого текущей директории (или указанной)."""
        # Если передан аргумент, будем считать это путем к каталогу.
        directory = self.args[0] if len(self.args) > 0 else os.getcwd()

        try:
            # Получаем список файлов и директорий в каталоге.
            for item in os.listdir(directory):
                self.stdout.write(f'{item}\n')

            return 0  # Успешное завершение.
        except FileNotFoundError:
            self.stdout.write(f'Ошибка: Директория {directory} не найдена.\n')
            return 1  # Ошибка - директория не найдена.
        except PermissionError:
            self.stdout.write(f'Ошибка: Недостаточно прав для доступа к {directory}.\n')
            return 1  # Ошибка доступа.
