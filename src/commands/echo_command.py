from src.commands.base_command import BaseCommand


class EchoCommand(BaseCommand):
    def __call__(self, user_string: str) -> int:
        return self.stdout.write(user_string)
