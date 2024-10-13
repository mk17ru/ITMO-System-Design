import subprocess

import cli.commands.base_command as base_command


class ExternalCommand(base_command.BaseCommand):
    """ExternalCommand logic."""

    def __call__(self) -> int:
        """Summary of __call__.

        Returns:
            int: Description of return value
        """
        command = self.args[0]

        """Summary of __call__.

        Args:
            command (str): Description of command.

        Returns:
            int: Description of return value
        """
        if isinstance(command, str):
            return subprocess.run(command.split(), stdin=self.stdin, stdout=self.stdout).returncode
        raise TypeError
