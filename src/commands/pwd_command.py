import os

from src.commands.base_command import BaseCommand


class PwdCommand(BaseCommand):
    def __call__(self) -> int:
        self.stdout.write(os.getcwd())
        return 0
