import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
from pathlib import Path
from src.commands.cat_command import CatCommand


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

        ret_code = cat_command(test_path)

        assert cat_command.stdout.getvalue() == test_content
        assert ret_code == 0

    @patch('builtins.open', create=True)
    def test_cat_command_file_not_found(self, mock_open, cat_command):
        mock_open.side_effect = FileNotFoundError

        test_path = Path('non_existent_file.txt')

        ret_code = cat_command(test_path)

        assert ret_code == 1

    @patch('builtins.open', create=True)
    def test_cat_command_permission_error(self, mock_open, cat_command):
        mock_open.side_effect = PermissionError

        test_path = Path('restricted_file.txt')

        ret_code = cat_command(test_path)

        assert ret_code == 1

    @patch('builtins.open', create=True)
    def test_cat_command_unexpected_error(self, mock_open, cat_command):
        mock_open.side_effect = Exception('Unexpected error')

        test_path = Path('some_file.txt')

        ret_code = cat_command(test_path)

        assert ret_code == 1
