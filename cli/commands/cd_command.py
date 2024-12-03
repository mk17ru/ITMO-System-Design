import os

import cli.commands.base_command as base_command


class CdCommand(base_command.BaseCommand):
    """Command to change the current working directory."""

    def __call__(self) -> int:
        """Change the working directory.

        Returns:
            int: 0 if directory changed successfully, 1 if error occurs.
        """
        if not self.args:
            self.stdout.write('cd: missing argument\n')
            return 1

        new_dir = self.args[0]

        if not os.path.exists(new_dir):
            self.stdout.write(f'cd: no such file or directory: {new_dir}\n')
            return 1

        if not os.path.isdir(new_dir):
            self.stdout.write(f'cd: not a directory: {new_dir}\n')
            return 1

        try:
            os.chdir(new_dir)
            return 0
        except PermissionError:
            self.stdout.write(f'cd: permission denied: {new_dir}\n')
        return 1
