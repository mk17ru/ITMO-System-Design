import re
import argparse
from typing import List, Any

from cli.commands.base_command import BaseCommand


class GrepCommand(BaseCommand):
    """Command for searching patterns in files, similar to Unix grep."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.context_lines = 0
        self.ignore_case = False
        self.match_whole_word = False
        self.pattern = ""
        self.file_path = ""
        self.args = []

    def set_args(self, args: list[Any]) -> None:
        """Sets the arguments for the command."""
        self.args = args

    def parse_args(self) -> None:
        """Parse arguments for the grep command."""
        parser = argparse.ArgumentParser(description="Search for patterns in files.")
        parser.add_argument("pattern", type=str, help="Regular expression to search for")
        parser.add_argument("file", type=str, help="File to search")
        parser.add_argument("-w", action="store_true", help="Match the whole word")
        parser.add_argument("-i", action="store_true", help="Ignore case")
        parser.add_argument("-A", type=int, default=0, help="Print specified number of lines after match")

        parsed_args = parser.parse_args(self.args)
        self.pattern = parsed_args.pattern
        self.file_path = parsed_args.file
        self.match_whole_word = parsed_args.w
        self.ignore_case = parsed_args.i
        self.context_lines = parsed_args.A

    def __call__(self) -> int:
        """Execute grep command logic."""
        # First, parse the arguments
        self.parse_args()

        flags = re.IGNORECASE if self.ignore_case else 0
        pattern = r"\b" + self.pattern + r"\b" if self.match_whole_word else self.pattern
        regex = re.compile(pattern, flags)

        try:
            with open(self.file_path, 'r') as lines:

                matches = []

                for i, line in enumerate(lines):
                    if regex.search(line):
                        start, end = i, i + self.context_lines + 1
                        matches.extend(lines[j] for j in range(start, min(end, len(lines))))

                self.stdout.write("".join(matches))
            return 0

        except FileNotFoundError:
            self.stdout.write(f"File not found: {self.file_path}\n")
            return 1
