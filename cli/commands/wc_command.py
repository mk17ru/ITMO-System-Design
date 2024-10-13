from pathlib import Path
from typing import TextIO

import cli.commands.base_command as base_command


class WcCommand(base_command.BaseCommand):
    """WcCommand logic."""

    @staticmethod
    def _compute_statistics(iostream: TextIO) -> tuple[int, int, int]:
        """Summary of _compute_statistics.

        Args:
            iostream (TextIO): Description of iostream.

        Returns:
            Tuple[int, int, int]: Description of return value
        """
        bts, words, lines = 0, 0, 0
        for line in iostream:
            lines += 1
            words += len(line.strip().split())
            bts += len(line)
        return lines, words, bts

    def __call__(self) -> int:
        """Summary of __call__.

        Returns:
            int: Description of return value
        """
        path: Path | None = None

        if len(self.args) != 0:
            path = self.args[0]

        if path is not None:
            with open(path) as file:
                lines, words, bts = self._compute_statistics(file)
        else:
            lines, words, bts = self._compute_statistics(self.stdin)
        self.stdout.write(f"{lines} {words} {bts} {path or ''}")
        return 0
