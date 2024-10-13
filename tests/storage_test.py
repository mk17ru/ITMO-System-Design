from cli.storage import Storage


def test_storage_add_and_get():
    storage = Storage()
    storage.add("key1", "value1")
    storage.add("key2", 123)

    assert storage.get("key1") == "value1"
    assert storage.get("key2") == 123


def test_storage_get_non_existent_key():
    storage = Storage()
    assert storage.get("nonexistent") == None


def test_storage_add_overwrite():
    storage = Storage()
    storage.add("key1", "value1")
    storage.add("key1", "new_value")

    assert storage.get("key1") == "new_value"
