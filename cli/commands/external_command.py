import subprocess

import cli.commands.base_command as base_command


class ExternalCommand(base_command.BaseCommand):
    """ExternalCommand logic."""

    def __call__(self, command: str) -> int:
        """Summary of __call__.

        Args:
            command (str): Description of command.

        Returns:
            int: Description of return value
        """
        return subprocess.run(command.split(), stdin=self.stdin, stdout=self.stdout).returncode
