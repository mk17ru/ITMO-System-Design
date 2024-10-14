import pytest

from cli.commands.exit_command import ExitCommand


class TestExitCommand:
    @pytest.fixture
    def exit_command(self):
        return ExitCommand()

    def test_echo_command_exit(self, exit_command):
        status_code = exit_command()

        assert status_code == 0
