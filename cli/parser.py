import typing

import cli.commands.base_command as base_command
import cli.commands.cat_command as cat_command
import cli.commands.echo_command as echo_command
import cli.commands.exit_command as exit_command
import cli.commands.external_command as external_command
import cli.commands.pwd_command as pwd_command
import cli.commands.wc_command as wc_command


class Parser:
    """Parser logic."""

    def parse(self, text: str) -> typing.List[base_command.BaseCommand]:
        """Summary of parse.

        Args:
            text (str): Description of text.

        Returns:
            typing.List[base_command.BaseCommand]: Description of return value
        """
        result: typing.List[base_command.BaseCommand] = []

        for line in text.split('\n'):
            line.strip()
            line = line.split()
            if len(line) == 0:
                continue
            cmd_str = line[0]
            args = line[1:]
            args = [arg for arg in args if arg != '']
            if cmd_str == 'cat':
                if len(args) != 1:
                    raise Exception('Wrong number of arguments!')
                cmd = cat_command.CatCommand()
                cmd.set_args(args)
                result.append(cmd)
            elif cmd_str == 'echo':
                if len(args) == 0:
                    raise Exception('Wrong number of arguments!')
                cmd = echo_command.EchoCommand()
                cmd.set_args([''.join(args)])
                result.append(cmd)
            elif cmd_str == 'exit':
                if len(args) != 0:
                    raise Exception('Wrong number of arguments!')
                result.append(exit_command.ExitCommand())
            elif cmd_str == 'pwd':
                if len(args) != 0:
                    raise Exception('Wrong number of arguments!')
                result.append(pwd_command.PwdCommand())
            elif cmd_str == 'wc':
                if len(args) != 1:
                    raise Exception('Wrong number of arguments!')
                cmd = wc_command.WcCommand()
                cmd.set_args(args)
                result.append(cmd)
            else:
                result.append(external_command.ExternalCommand())

        return result
