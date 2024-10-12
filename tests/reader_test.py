import io
from cli.reader import Reader



def test_read_stringio():
    input_stream = io.StringIO("Hello, World!")
    reader = Reader()
    result = reader.read(input_stream)
    assert result == 'Hello, World!'


def test_read_empty_stream():
    input_stream = io.StringIO("")
    reader = Reader()
    result = reader.read(input_stream)
    assert result == ''


def test_read_file():
    reader = Reader()
    with open("testfile.txt", "w") as f:
        f.write("File content")

    with open("testfile.txt", "r") as f:
        result = reader.read(f)
        assert result == "File content"

