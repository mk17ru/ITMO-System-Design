import typing
import sys


class Presenter:
    def __init__(self, output_stream: typing.TextIO = sys.stdout) -> None:
        self.output_stream = output_stream

    """
    """

    def show(self, message: str) -> None:
        self.output_stream.write(message + '\n')
        self.output_stream.flush()
