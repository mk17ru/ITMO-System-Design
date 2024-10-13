from cli import executor, parser, presenter, reader
from cli.commands import base_command


def main_logic() -> int:
    """Implement main flow of CLI."""
    while True:
        try:
            raw_input_command: str = reader.Reader.read()
            parsed_commands: list[base_command.BaseCommand] = parser.Parser.parse(raw_input_command)
            executor.Executor.execute(parsed_commands)
            presenter_ = presenter.Presenter()
            print(executor.Executor.output_data)
            presenter_.show(executor.Executor.output_data)
        except KeyboardInterrupt:
            return 0


if __name__ == '__main__':
    main_logic()
