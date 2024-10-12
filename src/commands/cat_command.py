from pathlib import Path


from src.commands.base_command import BaseCommand


class CatCommand(BaseCommand):
    def __call__(self, path: Path) -> int:
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
