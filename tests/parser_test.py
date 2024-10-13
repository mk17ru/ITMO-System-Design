import pytest

import cli.commands.cat_command as cat_command
import cli.commands.echo_command as echo_command
import cli.commands.exit_command as exit_command
import cli.commands.external_command as external_command
import cli.commands.pwd_command as pwd_command
import cli.commands.wc_command as wc_command
from cli.parser import Parser


def test_parse_command_with_argument():
    parser = Parser()
    result = parser.parse('cat file.txt')
    assert len(result) == 1
    assert isinstance(result[0], cat_command.CatCommand)
    assert len(result[0].args) == 1
    assert result[0].args[0] == 'file.txt'


def test_parse_command_with_argument_quotes():
    parser = Parser()
    result = parser.parse("cat 'file.txt'")
    assert len(result) == 1
    assert isinstance(result[0], cat_command.CatCommand)
    assert len(result[0].args) == 1
    assert result[0].args[0] == "'file.txt'"


def test_parse_command_without_arguments():
    parser = Parser()
    result = parser.parse('pwd')
    assert len(result) == 1
    assert isinstance(result[0], pwd_command.PwdCommand)
    assert len(result[0].args) == 0


def test_parse_command_wrong_arguments():
    parser = Parser()
    with pytest.raises(Exception, match='Wrong number of arguments!'):
        parser.parse('pwd wrong_argument')


def test_parse_multiple_commands():
    parser = Parser()
    commands_text = """cat file.txt
echo some text
wc file.txt

pwd
exit
external_command argument"""
    result = parser.parse(commands_text)
    assert len(result) == 6
    assert isinstance(result[0], cat_command.CatCommand)
    assert isinstance(result[1], echo_command.EchoCommand)
    assert isinstance(result[2], wc_command.WcCommand)
    assert isinstance(result[3], pwd_command.PwdCommand)
    assert isinstance(result[4], exit_command.ExitCommand)
    assert isinstance(result[5], external_command.ExternalCommand)
