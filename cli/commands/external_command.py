import io
import subprocess

import cli.commands.base_command as base_command


class ExternalCommand(base_command.BaseCommand):
    """ExternalCommand logic."""

    def __call__(self) -> int:
        """Summary of __call__.

        Returns:
            int: Cmd return code
        """
        command = self.args

        result = subprocess.run(command, stdin=self.stdin, capture_output=True)
        self.stdout.write(result.stdout.decode())
        self.stdout.flush()
        return result.returncode
