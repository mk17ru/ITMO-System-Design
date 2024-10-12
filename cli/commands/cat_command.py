import pathlib

import cli.commands.base_command as base_command


class CatCommand(base_command.BaseCommand):
    """CatCommand logic."""

    def __call__(self, path: pathlib.Path) -> int:
        """Summary of __call__.

        Args:
            path (pathlib.Path): Description of path.

        Returns:
            int: Description of return value
        """
        try:
            with open(path, 'r') as file:
                for line in file:
                    if not (ret_code := self.stdout.write(line)):
                        return ret_code
        except FileNotFoundError:
            print('Error: The file was not found.')
            return 1
        except PermissionError:
            print('Error: You do not have permission to open this file.')
            return 1
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return 1
        return 0
