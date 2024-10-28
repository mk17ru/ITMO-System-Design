import re
import subprocess

import cli.commands.base_command as base_command
import cli.commands.cat_command as cat_command
import cli.commands.echo_command as echo_command
import cli.commands.exit_command as exit_command
import cli.commands.external_command as external_command
import cli.commands.grep_command as grep_command
import cli.commands.pwd_command as pwd_command
import cli.commands.wc_command as wc_command
from cli.storage import Storage


class InvalidCommandError(ValueError):
    """Raise if input cmd is not Linux command."""

    pass


class Parser:
    """Parser logic."""

    def __init__(self) -> None:
        self.storage = Storage()

    PIPE_SYMBOL = '|'

    @staticmethod
    def _is_valid_cmd(cmd: str) -> bool:
        """Summary of _is_valid_cmd.

        Args:
            cmd (str): Check that input cmd is Linux acceptable cmd

        Returns:
            bool: Is cmd is Linux cmd?
        """
        result = subprocess.run(
            [base_command.Commands.WHICH, cmd],
            capture_output=True,
        )
        return any([
            result.returncode == 0,
            cmd == 'exit',  # we support exit cmd in our CLI
        ])

    @staticmethod
    def _validate_input_cmd(input_cmd: str) -> None:
        """Summary of _validate_input_cmd.

        Args:
            input_cmd (str): Cmd to validate

        Returns:
            None
        """
        if not Parser._is_valid_cmd(input_cmd):
            raise InvalidCommandError(f'Command {input_cmd} is not valid Linux command!')
        return None

    def parse(self, cli_input: str) -> list[base_command.BaseCommand]:
        """Summary of parse.

        Args:
            cli_input (str): CLI user input as a string

        Returns:
            typing.List[base_command.BaseCommand]: Parsed commands
        """
        result: list[base_command.BaseCommand] = []
        for cmd_line in cli_input.split(Parser.PIPE_SYMBOL):
            cmd_line.strip()
            cmd_line_splitted = cmd_line.split()
            if len(cmd_line_splitted) == 0:
                continue
            filtered_tokens = []
            for token in cmd_line_splitted:
                if re.match(r'^[A-Za-z_]\w*=\S+$', token):
                    key, value = token.split('=', 1)
                    self.storage.set(key, value)
                    continue
                elif re.match(r'^\$[A-Za-z_]\w*$', token):
                    key = token[1:]
                    val = self.storage.get(key)
                    filtered_tokens.append(val)
                else:
                    filtered_tokens.append(token)
            if len(filtered_tokens) == 0:
                continue

            input_cmd = filtered_tokens[0]
            Parser._validate_input_cmd(input_cmd)
            args = filtered_tokens[1:]
            args = [arg for arg in args if arg != '']
            match input_cmd:
                case base_command.Commands.CAT:
                    if len(args) != 1:
                        raise Exception('Wrong number of arguments!')
                    cat_cmd = cat_command.CatCommand()
                    cat_cmd.set_args(args)
                    result.append(cat_cmd)
                case base_command.Commands.ECHO:
                    if len(args) == 0:
                        raise Exception('Wrong number of arguments!')
                    echo_cmd = echo_command.EchoCommand()
                    echo_cmd.set_args([''.join(args)])
                    result.append(echo_cmd)
                case base_command.Commands.EXIT:
                    if len(args) != 0:
                        raise Exception('Wrong number of arguments!')
                    result.append(exit_command.ExitCommand())
                case base_command.Commands.PWD:
                    if len(args) != 0:
                        raise Exception('Wrong number of arguments!')
                    result.append(pwd_command.PwdCommand())
                case base_command.Commands.WC:
                    if len(args) != 1:
                        raise Exception('Wrong number of arguments!')
                    wc_cmd = wc_command.WcCommand()
                    wc_cmd.set_args(args)
                    result.append(wc_cmd)
                case base_command.Commands.GREP:
                    if len(args) < 2:
                        raise Exception('Wrong number of arguments!')
                    grep_cmd = grep_command.GrepCommand()
                    grep_cmd.set_args(args)
                    result.append(grep_cmd)
                case _:
                    external_cmd = external_command.ExternalCommand()
                    args.insert(0, input_cmd)
                    external_cmd.set_args(args)
                    result.append(external_cmd)
        return result
