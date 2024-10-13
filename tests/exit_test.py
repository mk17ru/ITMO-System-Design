import pytest
from unittest.mock import patch
from cli.commands.exit_command import ExitCommand


class TestExitCommand:
    @pytest.fixture
    def exit_command(self):
        return ExitCommand()

    def test_echo_command_exit(self, exit_command):
        with pytest.raises(SystemExit) as exc_info:
            exit_command()

        assert exc_info.type == SystemExit
        assert exc_info.value.code == 0
