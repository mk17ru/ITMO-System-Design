from io import StringIO
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from cli.commands.wc_command import WcCommand


class TestWcCommand:
    @pytest.fixture
    def wc_command(self):
        mock_stdout = StringIO()
        command = WcCommand(stdout=mock_stdout)
        return command

    @patch('builtins.open', create=True)
    def test_wc_command_file_input(self, mock_open, wc_command):
        test_content = 'Hello world\nTest\n'
        mock_file = MagicMock()
        mock_file.__enter__.return_value = test_content.splitlines(True)
        mock_open.return_value = mock_file

        test_path = Path('test_file.txt')
        wc_command.set_args([test_path])

        ret_code = wc_command()

        assert wc_command.stdout.getvalue() == '2 3 17 test_file.txt'
        assert ret_code == 0

    def test_wc_command_stdin_input(self, wc_command):
        wc_command.stdin = StringIO('Hello world\nTest\n')

        ret_code = wc_command()

        assert wc_command.stdout.getvalue() == '2 3 17 '
        assert ret_code == 0
