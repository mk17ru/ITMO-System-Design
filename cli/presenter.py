import sys

class Presenter:
    def __init__(self, output_stream=sys.stdout):
        self.output_stream = output_stream

    """Метод вывода сообщения в поток."""
    def Show(self, message: str):
        self.output_stream.write(message + '\n')
        self.output_stream.flush()
