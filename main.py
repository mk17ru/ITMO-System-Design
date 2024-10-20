from cli import executor, parser, presenter, reader
from cli.commands import base_command


def main_logic() -> int:
    """Implement main flow of CLI."""
    parser_implementaion = parser.Parser()
    while True:
        try:
            raw_input_command: str = reader.Reader.read()
            parsed_commands: list[base_command.BaseCommand] = parser_implementaion.parse(raw_input_command)
            executor.Executor.execute(parsed_commands)
            presenter_ = presenter.Presenter()
            presenter_.show(executor.Executor.output_data)
        except parser.InvalidCommandError as exc:
            print(exc)
        except KeyboardInterrupt:
            return 0


if __name__ == '__main__':
    main_logic()
