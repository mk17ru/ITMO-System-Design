from cli.commands import base_command


OK_STATUS_CODE = 0
ERROR_STATUS_CODE = 1


class Executor:
    """Executor logic."""

    output_data: str = ''

    @staticmethod
    def execute(parsed_commands: list[base_command.BaseCommand]) -> int:
        """Summary of execute.

        Args:
            parsed_commands (list[base_command.BaseCommand]): List of parsed_commands.

        Returns:
            int: Status code
        """
        status_code: int = OK_STATUS_CODE
        error_message = None
        try:
            for _, command in enumerate(parsed_commands):
                status_code = command()
                # output_io = io.StringIO()
                # with contextlib.redirect_stdout(output_io): doesn't work correctly
                #     Executor.output_data = output_io.getvalue()
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
