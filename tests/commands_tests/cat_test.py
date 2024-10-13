from io import StringIO
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from cli.commands.cat_command import CatCommand


class TestCatCommand:
    @pytest.fixture
    def cat_command(self):
        mock_stdout = StringIO()
        command = CatCommand(stdout=mock_stdout)
        return command

    @patch('builtins.open', create=True)
    def test_cat_command_reads_and_writes(self, mock_open, cat_command):
        test_content = 'Hello, this is a test file.'
        mock_file = MagicMock()
        mock_file.__enter__.return_value = test_content.splitlines(True)
        mock_open.return_value = mock_file

        test_path = Path('test_file.txt')
        cat_command.set_args([test_path])

        ret_code = cat_command()

        assert cat_command.stdout.getvalue() == test_content
        assert ret_code == 0
