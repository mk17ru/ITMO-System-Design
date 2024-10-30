import tempfile

from cli.commands.external_command import ExternalCommand


def test_external_command():
    with tempfile.NamedTemporaryFile('w+') as stdout_file, tempfile.NamedTemporaryFile('r+') as input_file:
        cmd = ExternalCommand(stdin=input_file, stdout=stdout_file)
        input_cmd = 'head -n 1 tests/commands_tests/exit_test.py'.split()
        cmd.set_args(input_cmd)
        ret_code = cmd()

        stdout_file.seek(0)
        output = stdout_file.read()
        expected_out = """import pytest\n"""

        assert ret_code == 0
        assert output == expected_out
