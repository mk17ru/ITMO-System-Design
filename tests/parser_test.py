import pytest

import cli.commands.cat_command as cat_command
import cli.commands.echo_command as echo_command
import cli.commands.exit_command as exit_command
import cli.commands.external_command as external_command
import cli.commands.grep_command as grep_command
import cli.commands.pwd_command as pwd_command
import cli.commands.wc_command as wc_command
from cli import parser
from cli.commands import ls_command


def test_parse_command_with_argument():
    parser_ = parser.Parser()
    result = parser_.parse('cat file.txt')

    assert len(result) == 1
    assert isinstance(result[0], cat_command.CatCommand)
    assert len(result[0].args) == 1
    assert result[0].args[0] == 'file.txt'


def test_parse_command_with_argument_quotes():
    parser_ = parser.Parser()
    result = parser_.parse("cat 'file'")

    assert len(result) == 1
    assert isinstance(result[0], cat_command.CatCommand)
    assert len(result[0].args) == 1
    assert result[0].args[0] == 'file'


def test_parse_command_without_arguments():
    parser_ = parser.Parser()
    result = parser_.parse('pwd')

    assert len(result) == 1
    assert isinstance(result[0], pwd_command.PwdCommand)
    assert len(result[0].args) == 0


def test_parse_command_wrong_arguments():
    parser_ = parser.Parser()
    with pytest.raises(Exception, match='Wrong number of arguments!'):
        result = parser_.parse('pwd wrong_argument')

        assert len(result) == 0


def test_parse_multiple_commands():
    parser_ = parser.Parser()
    commands_text = """ 
                    cat file.txt | 
                    echo some text | 
                    wc file.txt | 
                    pwd | 
                    grep f file.txt |
                    ls argument |
                    exit
                    """
    result = parser_.parse(commands_text)
    assert len(result) == 7

    assert isinstance(result[0], cat_command.CatCommand)
    assert isinstance(result[1], echo_command.EchoCommand)
    assert isinstance(result[2], wc_command.WcCommand)
    assert isinstance(result[3], pwd_command.PwdCommand)
    assert isinstance(result[4], grep_command.GrepCommand)
    assert isinstance(result[5], ls_command.LsCommand)
    assert isinstance(result[6], exit_command.ExitCommand)


def test_parse_external_command():
    parser_ = parser.Parser()
    result = parser_.parse('lsof')

    assert len(result) == 1
    assert isinstance(result[0], external_command.ExternalCommand)
    assert len(result[0].args) == 1


def test_parse_wrong_command():
    parser_ = parser.Parser()
    input_cmd = 'my_beautiful_cmd arg1'
    with pytest.raises(
        parser.InvalidCommandError,
        match=f'Command {input_cmd.split()[0]} is not valid Linux command!',
    ):
        result = parser_.parse(input_cmd)

        assert len(result) == 0


def test_parse_from_storage():
    parser_ = parser.Parser()

    parser_.parse('alias=pwd')

    result = parser_.parse('$alias')

    assert len(result) == 1
    assert isinstance(result[0], pwd_command.PwdCommand)
    assert len(result[0].args) == 0


def test_parse_set_and_echo():
    parser_ = parser.Parser()

    parser_.parse('x=1')

    result = parser_.parse('echo $x')

    assert len(result) == 1
    assert isinstance(result[0], echo_command.EchoCommand)
    assert result[0].args[0] == '1'


def test_parse_from_set_command():
    parser_ = parser.Parser()

    parser_.parse('x=1')

    result = parser_.parse('x=echo | $x 1')

    assert len(result) == 1
    assert isinstance(result[0], echo_command.EchoCommand)
    assert result[0].args[0] == '1'


def test_parse_from_set_quote_double():
    parser_ = parser.Parser()

    parser_.parse('x=1')

    result = parser_.parse('x=1 | echo "123$x"')

    assert len(result) == 1
    assert isinstance(result[0], echo_command.EchoCommand)
    assert result[0].args[0] == '1231'


def test_parse_from_set_quote():
    parser_ = parser.Parser()

    parser_.parse('x=1')

    result = parser_.parse("x=1 | echo '123$x'")

    assert len(result) == 1
    assert isinstance(result[0], echo_command.EchoCommand)
    assert result[0].args[0] == '1231'


def test_parse_from_set_quote_whitespace():
    parser_ = parser.Parser()

    parser_.parse('x=1')

    result = parser_.parse("x=1 | echo '1$x 23'")

    assert len(result) == 1
    assert isinstance(result[0], echo_command.EchoCommand)
    assert result[0].args[0] == '11 23'


def test_parse_from_set_multi_quote_double():
    parser_ = parser.Parser()

    parser_.parse('x=1')
    parser_.parse('y=9')

    result = parser_.parse('x=1 | echo "123$x$y $x test"')

    assert len(result) == 1
    assert isinstance(result[0], echo_command.EchoCommand)
    assert result[0].args[0] == '12319 1 test'


def test_parse_from_set_quote_command_several():
    parser_ = parser.Parser()

    parser_.parse('x=rrr')
    result = parser_.parse('"echo" 123')
    result_quotes = parser_.parse('echo " \'$x\' "')

    assert len(result) == 1
    assert isinstance(result[0], echo_command.EchoCommand)
    assert result[0].args[0] == '123'

    assert len(result_quotes) == 1
    assert isinstance(result_quotes[0], echo_command.EchoCommand)
    assert result_quotes[0].args[0] == " 'rrr' "


def test_parse_grep_command():
    parser_ = parser.Parser()

    result = parser_.parse('grep "Минимальный" README.md')

    assert len(result) == 1
    assert isinstance(result[0], grep_command.GrepCommand)
    assert result[0].args[0] == 'Минимальный'
    assert result[0].args[1] == 'README.md'


def test_parse_cat_command():
    parser_ = parser.Parser()

    result = parser_.parse('cat "README".md')

    assert len(result) == 1
    assert isinstance(result[0], cat_command.CatCommand)
    assert result[0].args[0] == 'README.md'
