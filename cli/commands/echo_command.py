import cli.commands.base_command as base_command


class EchoCommand(base_command.BaseCommand):
    """EchoCommand logic."""

    def __call__(self) -> int:
        user_string: str = self.args[0]

        """Summary of __call__.

        Args:
            user_string (str): Description of user_string.

        Returns:
            int: Description of return value
        """
        return self.stdout.write(user_string)
