import os
from io import StringIO
from unittest.mock import patch
import pytest

from cli.commands.ls_command import LsCommand


class TestLsCommand:
    @pytest.fixture
    def ls_command(self):
        mock_stdout = StringIO()
        command = LsCommand(stdout=mock_stdout)
        return command

    @patch("os.listdir")
    @patch("os.getcwd", return_value="/mocked/directory")
    def test_ls_command_no_args(self, mock_getcwd, mock_listdir, ls_command):
        mock_listdir.return_value = ["file1", "file2", "dir1"]

        ret_code = ls_command()

        assert ls_command.stdout.getvalue() == "file1\nfile2\ndir1\n"
        assert ret_code == 0

    @patch("os.listdir")
    def test_ls_command_with_args(self, mock_listdir, ls_command):
        mock_listdir.return_value = ["file1", "file2", "dir1"]
        test_path = "/custom/directory"
        ls_command.set_args([test_path])

        ret_code = ls_command()

        assert ls_command.stdout.getvalue() == "file1\nfile2\ndir1\n"
        assert ret_code == 0

    @patch("os.listdir", side_effect=FileNotFoundError)
    def test_ls_command_directory_not_found(self, mock_listdir, ls_command):
        test_path = "/non_existent/directory"
        ls_command.set_args([test_path])

        ret_code = ls_command()

        assert (
            ls_command.stdout.getvalue()
            == "Ошибка: Директория /non_existent/directory не найдена.\n"
        )
        assert ret_code == 1

    @patch("os.listdir", side_effect=PermissionError)
    def test_ls_command_permission_denied(self, mock_listdir, ls_command):
        test_path = "/restricted/directory"
        ls_command.set_args([test_path])

        ret_code = ls_command()

        assert (
            ls_command.stdout.getvalue()
            == "Ошибка: Недостаточно прав для доступа к /restricted/directory.\n"
        )
        assert ret_code == 1
