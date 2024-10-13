import io
import os
import uuid

from cli.reader import Reader


def test_read_stringio():
    input_stream = io.StringIO('Hello, World!')
    reader = Reader()
    result = reader.read(input_stream)
    assert result == 'Hello, World!'


def test_read_empty_stream():
    input_stream = io.StringIO('')
    reader = Reader()
    result = reader.read(input_stream)
    assert result == ''


def test_read_file():
    reader = Reader()

    isolate_postfix = uuid.uuid4().hex[:6]
    test_file_path = f'testfile_{isolate_postfix}.txt'

    with open(test_file_path, 'w') as f:
        f.write('File content')
    try:
        with open(test_file_path) as f:
            result = reader.read(f)
            assert result == 'File content'
    finally:
        os.remove(test_file_path)
