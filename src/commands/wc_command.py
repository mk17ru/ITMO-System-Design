from pathlib import Path
from typing import Optional, TextIO, Tuple

from src.commands.base_command import BaseCommand


class WcCommand(BaseCommand):
    @staticmethod
    def _compute_statistics(istream: TextIO) -> Tuple[int, int, int]:
        bts, words, lines = 0, 0, 0
        for line in istream:
            lines += 1
            words += len(line.split())
            bts += len(line)
        return (lines, words, bts)

    def __call__(self, path: Optional[Path] = None) -> int:
        if path is not None:
            try:
                with open(path, 'r') as file:
                    lines, words, bts = self._compute_statistics(file)
            except FileNotFoundError:
                print('Error: The file was not found.')
                return 1
            except PermissionError:
                print('Error: You do not have permission to open this file.')
                return 1
            except Exception as e:
                print(f'An unexpected error occurred: {e}')
                return 1
        else:
            lines, words, bts = self._compute_statistics(self.stdin)
        self.stdout.write(f"{lines} {words} {bts} {path or ''}")
        return 0
