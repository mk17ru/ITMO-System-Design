import subprocess

from src.commands.base_command import BaseCommand


class ExternalCommand(BaseCommand):
    def __call__(self, command: str) -> int:
        return subprocess.run(command.split(), stdin=self.stdin, stdout=self.stdout).returncode
