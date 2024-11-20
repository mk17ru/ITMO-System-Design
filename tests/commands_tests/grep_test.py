from io import StringIO
from unittest.mock import MagicMock, patch

import pytest

from cli.commands.grep_command import GrepCommand


class TestGrepCommand:
    @pytest.fixture
    def grep_command(self):
        mock_stdout = StringIO()
        command = GrepCommand(stdout=mock_stdout)
        return command

    @patch('builtins.open', create=True)
    def test_grep_basic(self, mock_open, grep_command):
        test_content = 'This is a test line.\nAnother line.\npattern line.\n'
        mock_file = MagicMock()
        mock_file.__enter__.return_value = test_content.splitlines(True)
        mock_open.return_value = mock_file

        grep_command.set_args(['pattern', 'test_file.txt'])

        ret_code = grep_command()

        assert grep_command.stdout.getvalue() == 'pattern line.\n'
        assert ret_code == 0

    @patch('builtins.open', create=True)
    def test_grep_ignore_case(self, mock_open, grep_command):
        test_content = 'pattern in lowercase.\nPattern uppercase.\n'
        mock_file = MagicMock()
        mock_file.__enter__.return_value = test_content.splitlines(True)
        mock_open.return_value = mock_file

        grep_command.set_args(['pattern', 'test_file.txt', '-i'])

        ret_code = grep_command()

        assert grep_command.stdout.getvalue() == 'pattern in lowercase.\nPattern uppercase.\n'
        assert ret_code == 0

    @patch('builtins.open', create=True)
    def test_grep_whole_word(self, mock_open, grep_command):
        test_content = 'This is patternalism.\npattern here.\n'
        mock_file = MagicMock()
        mock_file.__enter__.return_value = test_content.splitlines(True)
        mock_open.return_value = mock_file

        grep_command.set_args(['pattern', 'test_file.txt', '-w'])

        ret_code = grep_command()

        assert grep_command.stdout.getvalue() == 'pattern here.\n'
        assert ret_code == 0

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open, grep_command):
        grep_command.set_args(['pattern', 'nonexistent_file.txt'])

        ret_code = grep_command()

        assert grep_command.stdout.getvalue() == 'File not found: nonexistent_file.txt\n'
        assert ret_code == 1
