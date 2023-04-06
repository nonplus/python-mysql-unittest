# python-mysql-unittest

This example shows how to write Python MySQL unit tests

## Example overview

```
python-mysql-unittest/
├─ db /
│  ├─ datastore.py       # Datastore
├─ model/
│  ├─ student.py         # Student model
├─ tests/
│  ├─ test_datastore.py  # Datastore unit tests
│  ├─ test_setup.sql     # Test database initialization
```

### `db`

The [`Datastore` class](db/datastore.py) is used for reading and writing models to the database.

The constructor takes a database connection:

- In production, the production database connection would be supplied.
- For testing, the `testdb` connection is used

### `models`

The [`Student`](model/student.py) class is the in-memory representation of student records stored in the database.

### `tests`

Contains unit tests and associated test data.

#### [`test_datastore.py`](tests/test_datastore.py)

Unit tests for the `Datastore` class.

1. During setup, the database is initialized and a new `Datastore` object is instantiated
   - The database is reset before each test
2. Tests call methods on the `datastore` instance
   - The can update and query date using the the `datastore` methods or by directly creating a connection cursor.

#### [`test_setup.sql`](tests/test_setup.sql)

SQL executed before each test.  It should reset the database into a know state (e.g. recreating tables).

## Running the test

1. [Create a local database](/docs/create-temp-db.md) with the following settings:
   - Schema: `testdb`
   - User: `test`
   - Password: `test`
2.  If necessary, [install mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html)
3.  In the project directory, run the tests:
    ```
    python3 -m unittest discover -s tests
    ```
