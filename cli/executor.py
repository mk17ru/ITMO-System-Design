import io

from cli.commands import base_command


OK_STATUS_CODE = 0
ERROR_STATUS_CODE = 1


class Executor:
    """Executor logic."""

    output_data = io.StringIO()

    @staticmethod
    def execute(parsed_commands: list[base_command.BaseCommand]) -> int:
        """Summary of execute.

        Args:
            parsed_commands (list[base_command.BaseCommand]): List of parsed_commands.

        Returns:
            int: Status code
        """
        Executor.output_data = io.StringIO()
        status_code: int = OK_STATUS_CODE
        error_message = None
        try:
            for i, command in enumerate(parsed_commands):
                command.stdout = io.StringIO()

                if i + 1 == len(parsed_commands):
                    command.stdout = Executor.output_data
                status_code = command()
                if status_code == OK_STATUS_CODE:
                    if i + 1 != len(parsed_commands):
                        command.stdout.seek(0)
                        parsed_commands[i + 1].stdin = command.stdout
                else:
                    error_message = f'Error on command: {command.__class__.__name__}'
                    return status_code

        except FileNotFoundError:
            error_message = 'Error: The file was not found.'
        except PermissionError:
            error_message = 'Error: You do not have permission to open this file.'
        except Exception as e:
            error_message = f'An unexpected error occurred: {e}'
        finally:
            if error_message:
                print(error_message)
                status_code = ERROR_STATUS_CODE
        return status_code
