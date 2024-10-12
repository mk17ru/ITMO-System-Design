import typing


class Parser:
    def parse_string(self, line: str) -> None:
        splitted = line.split()
        cmd = splitted[0]
        if cmd == 'cat':
            print('cat')
