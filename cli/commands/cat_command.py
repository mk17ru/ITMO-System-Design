import pathlib

import cli.commands.base_command as base_command


class CatCommand(base_command.BaseCommand):
    """CatCommand logic."""

    def __call__(self) -> int:
        """Summary of __call__.

        Args:
            path (pathlib.Path): Description of path.

        Returns:
            int: Description of return value
        """
        path: pathlib.Path = self.args[0]

        with open(path) as file:
            for line in file:
                if not (ret_code := self.stdout.write(line)):
                    return ret_code
        return 0
