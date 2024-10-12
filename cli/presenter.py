import typing
import sys


class Presenter:
    def __init__(self, output_stream: typing.TextIO = sys.stdout) -> None:
        self.output_stream = output_stream

    def show(self, data: str) -> None:
        """

        :param data: str:
        :param data: str:
        :param data: str:

        """
        self.output_stream.write(data + '\n')
        self.output_stream.flush()
