from pathlib import Path
from typing import Optional, TextIO, Tuple

import base_command


class WcCommand(base_command.BaseCommand):
    """WcCommand logic."""

    @staticmethod
    def _compute_statistics(iostream: TextIO) -> Tuple[int, int, int]:
        """Summary of _compute_statistics.

        Args:
            iostream (TextIO): Description of iostream.

        Returns:
            Tuple[int, int, int]: Description of return value
        """
        bts, words, lines = 0, 0, 0
        for line in iostream:
            lines += 1
            words += len(line.split())
            bts += len(line)
        return lines, words, bts

    def __call__(self, path: Optional[Path] = None) -> int:
        """Summary of __call__.

        Args:
            path (Optional[Path]): Description of path. Default to None

        Returns:
            int: Description of return value
        """
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
