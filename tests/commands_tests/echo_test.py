import io

import pytest

from cli.commands.echo_command import EchoCommand


class TestEchoCommand:
    @pytest.fixture
    def echo_command(self):
        mock_stdout = io.StringIO()
        command = EchoCommand(stdout=mock_stdout)
        return command

    def test_echo_command_writes_string(self, echo_command):
        test_string = 'Hello, world!'
        echo_command.set_args([test_string])

        ret_code = echo_command()

        assert ret_code == 0
        assert echo_command.stdout.getvalue() == test_string
        assert len(echo_command.stdout.getvalue()) == len(test_string)

    def test_echo_command_writes_empty_string(self, echo_command):
        echo_command.set_args([''])
        bytes_written = len(echo_command.stdout.getvalue())

        ret_code = echo_command()

        assert ret_code == 0
        assert echo_command.stdout.getvalue() == ''
        assert bytes_written == 0
