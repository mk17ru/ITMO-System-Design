import os

import cli.commands.base_command as base_command


class LsCommand(base_command.BaseCommand):
    """Logic for the `ls` command."""

    def __call__(self) -> int:
        """Executes the `ls` command to display the contents of the current directory (or the specified one)."""
        # If an argument is provided, treat it as the directory path
        directory = self.args[0] if len(self.args) > 0 else os.getcwd()

        try:
            # Get the list of files and directories in the specified directory
            for item in os.listdir(directory):
                self.stdout.write(f'{item}\n')

            return 0  # Successful completion
        except FileNotFoundError:
            self.stdout.write(f'Error: Directory {directory} not found.\n')
            return 1  # Error - directory not found
        except PermissionError:
            self.stdout.write(f'Error: Insufficient permissions to access {directory}.\n')
            return 1  # Access error
