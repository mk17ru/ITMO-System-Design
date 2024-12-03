import os
import stat
from tempfile import TemporaryDirectory

import pytest

from cli.commands.cd_command import CdCommand


class TestCdCommand:
    @pytest.fixture(autouse=True)
    def setup_command(self):
        """Fixture to initialize CdCommand instance."""
        self.command = CdCommand()

    @pytest.fixture(scope='class', autouse=True)
    def change_and_restore_directory(self):
        """Fixture to save and restore the working directory for each test."""
        original_dir = os.getcwd()
        yield
        os.chdir(original_dir)

    def test_cd_to_valid_directory(self):
        with TemporaryDirectory() as temp_dir:
            self.command.set_args([temp_dir])
            assert self.command() == 0
            assert os.path.realpath(os.getcwd()) == os.path.realpath(temp_dir)

    def test_cd_to_nonexistent_directory(self):
        self.command.set_args(['/nonexistent_directory'])
        assert self.command() == 1

    def test_cd_without_arguments(self):
        self.command.set_args([])
        assert self.command() == 1

    def test_cd_permission_denied(self):
        with TemporaryDirectory() as temp_dir:
            # Устанавливаем права, запрещающие доступ
            os.chmod(temp_dir, stat.S_IRUSR)  # Только чтение для владельца

            # Проверяем переход в защищенную директорию
            self.command.set_args([temp_dir])
            assert self.command() == 1

            # Возвращаем права для корректного удаления временной директории
            os.chmod(temp_dir, stat.S_IRWXU)
