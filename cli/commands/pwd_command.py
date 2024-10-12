import os

import base_command


class PwdCommand(base_command.BaseCommand):
    """PwdCommand logic."""

    def __call__(self) -> int:
        """Summary of __call__.

        Returns:
            int: Description of return value
        """
        self.stdout.write(os.getcwd())
        return 0
