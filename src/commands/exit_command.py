import sys

from src.commands.base_command import BaseCommand


class ExitCommand(BaseCommand):
    def __call__(self) -> int:
        sys.exit(0)
