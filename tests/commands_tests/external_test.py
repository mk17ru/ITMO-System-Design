import os

from cli.commands.external_command import ExternalCommand


def test_external_command():
    with open('output.txt', 'w+') as stdout_file, open('input.txt', 'w+') as input_file:
        cmd = ExternalCommand(stdin=input_file, stdout=stdout_file)
        input_cmd = 'head -n 1 tests/commands_tests/external_test.py'.split()
        cmd.set_args(input_cmd)
        ret_code = cmd()

        stdout_file.seek(0)
        output = stdout_file.read()
        expected_out = """import os\n"""

        assert ret_code == 0
        assert output == expected_out
    os.remove('input.txt')
    os.remove('output.txt')
