from io import StringIO
from unittest.mock import patch

import pytest

from cli.commands.pwd_command import PwdCommand


class TestPwdCommand:
    @pytest.fixture
    def pwd_command(self):
        mock_stdout = StringIO()
        command = PwdCommand(stdout=mock_stdout)
        return command

    @patch('os.getcwd', return_value='/mocked/directory')
    def test_pwd_command(self, _, pwd_command):
        ret_code = pwd_command()

        assert pwd_command.stdout.getvalue() == '/mocked/directory'
        assert ret_code == 0
