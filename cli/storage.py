import typing


class Storage:
    def __init__(self):
        """Initialize the storage with an empty dictionary."""
        self.data: typing.Dict[str, typing.Any] = {}

    def add(self, key: str, val: typing.Any) -> None:
        """Adds a key-value pair to the storage."""
        self.data[key] = val

    def get(self, key: str) -> typing.Any:
        """Gets the value associated with the key from the storage.

        Returns None if the key is not present.
        """
        return self.data.get(key)
