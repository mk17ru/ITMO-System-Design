import sys

import base_command


class ExitCommand(base_command.BaseCommand):
    """ExitCommand logic."""

    def __call__(self) -> None:
        """Summary of __call__.

        Returns:
            None: Description of return value
        """
        sys.exit(0)
