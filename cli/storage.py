import typing


class Storage:
    """Storage logic."""

    def __init__(self) -> None:
        """Initialize the storage with an empty dictionary."""
        self.data: dict[str, typing.Any] = {}

    def set(self, key: str, val: typing.Any) -> None:
        """Adds a key-value pair to the storage."""
        self.data[key] = val

    def get(self, key: str) -> typing.Any:
        """Gets the value associated with the key from the storage.

        Returns None if the key is not present.
        """
        return self.data.get(key)
