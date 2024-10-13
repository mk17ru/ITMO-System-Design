import io
import os
import pathlib
import unittest.mock

import pytest

from cli import executor
from cli.commands import cat_command, echo_command, pwd_command, wc_command


@pytest.fixture
def _cat_command():
    mock_stdout = io.StringIO()
    command = cat_command.CatCommand(stdout=mock_stdout)
    return command


@pytest.fixture
def _wc_command():
    mock_stdout = io.StringIO()
    command = wc_command.WcCommand(stdout=mock_stdout)
    return command


@unittest.mock.patch('builtins.open', create=True)
def test_executor_cat_command(mock_open, _cat_command):
    test_content = 'Hello, this is a test file.'
    mock_file = unittest.mock.MagicMock()
    mock_file.__enter__.return_value = test_content.splitlines(True)
    mock_open.return_value = mock_file
    test_path = pathlib.Path('test_file.txt')
    _cat_command.set_args([test_path])

    executor_ = executor.Executor()
    ret_code = executor_.execute([_cat_command])

    assert ret_code == 0
    assert _cat_command.stdout.getvalue() == test_content


@unittest.mock.patch('builtins.open', create=True)
def test_executor_cat_command_file_not_found(mock_open, _cat_command):
    mock_open.side_effect = FileNotFoundError
    test_path = pathlib.Path('non_existent_file.txt')
    _cat_command.set_args([test_path])

    executor_ = executor.Executor()
    ret_code = executor_.execute([_cat_command])

    assert ret_code == 1


@unittest.mock.patch('builtins.open', create=True)
def test_executor_cat_command_permission_error(mock_open, _cat_command):
    mock_open.side_effect = PermissionError
    test_path = pathlib.Path('restricted_file.txt')
    _cat_command.set_args([test_path])

    executor_ = executor.Executor()
    ret_code = executor_.execute([_cat_command])

    assert ret_code == 1


@unittest.mock.patch('builtins.open', create=True)
def test_executor_cat_command_unexpected_error(mock_open, _cat_command):
    mock_open.side_effect = Exception('Unexpected error')
    test_path = pathlib.Path('some_file.txt')
    _cat_command.set_args([test_path])

    executor_ = executor.Executor()
    ret_code = executor_.execute([_cat_command])

    assert ret_code == 1


def test_executor_echo_command():
    stdout = io.StringIO()
    command = echo_command.EchoCommand(stdout=stdout)
    command.set_args(['Hello', 'World'])

    executor_ = executor.Executor()
    ret_code = executor_.execute([command])

    assert ret_code == 0
    assert stdout.getvalue() == 'Hello'


def test_executor_pwd_command():
    stdout = io.StringIO()
    command = pwd_command.PwdCommand(stdout=stdout)

    executor_ = executor.Executor()
    ret_code = executor_.execute([command])

    assert ret_code == 0
    assert stdout.getvalue().strip() == os.getcwd()


@unittest.mock.patch('builtins.open', create=True)
def test_executor_wc_command_with_file(mock_open, _wc_command):
    test_content = 'Hello world\nTest\n'
    mock_file = unittest.mock.MagicMock()
    mock_file.__enter__.return_value = test_content.splitlines(True)
    mock_open.return_value = mock_file

    test_path = pathlib.Path('test_file.txt')
    _wc_command.set_args([test_path])

    executor_ = executor.Executor()
    ret_code = executor_.execute([_wc_command])

    assert ret_code == 0
    assert _wc_command.stdout.getvalue() == '2 3 17 test_file.txt'


def test_executor_wc_command_without_file():
    stdin = io.StringIO('Line 1\nLine 2\nLine 3')
    stdout = io.StringIO()
    command = wc_command.WcCommand(stdin=stdin, stdout=stdout)

    executor_ = executor.Executor()
    ret_code = executor_.execute([command])

    assert ret_code == 0
    assert stdout.getvalue() == '3 6 20 '


@unittest.mock.patch('builtins.open', create=True)
def test_executor_wc_command_file_not_found(mock_open, _wc_command):
    mock_open.side_effect = FileNotFoundError
    test_path = pathlib.Path('non_existent_file.txt')
    _wc_command.set_args([test_path])

    executor_ = executor.Executor()
    ret_code = executor_.execute([_wc_command])

    assert ret_code == 1


@unittest.mock.patch('builtins.open', create=True)
def test_executor_wc_command_permission_error(mock_open, _wc_command):
    mock_open.side_effect = PermissionError
    test_path = pathlib.Path('restricted_file.txt')
    _wc_command.set_args([test_path])

    executor_ = executor.Executor()
    ret_code = executor_.execute([_wc_command])

    assert ret_code == 1


@unittest.mock.patch('builtins.open', create=True)
def test_executor_wc_command_unexpected_error(mock_open, _wc_command):
    mock_open.side_effect = Exception('Unexpected error')
    test_path = pathlib.Path('some_file.txt')
    _wc_command.set_args([test_path])

    executor_ = executor.Executor()
    ret_code = executor_.execute([_wc_command])

    assert ret_code == 1
