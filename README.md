# sqlalchemy-builder
[![PyPI version](https://badge.fury.io/py/sqlalchemy-builder.svg)](https://badge.fury.io/py/sqlalchemy-builder)

Build SQLAlchemy statements avoiding common footguns.

Check out the [documentation](https://jamie-chang.github.io/sqlalchemy-builder/)

## Example
Build select statements functionally using `|` and `|=`

```py
select(Model).where(Model.id == 1)
```
Becomes:

```py
from sqlalchemy_builder.select import where

select(Model) | where(Model.id == 1)
```

`|=` is also supported:
```py
statement = select(Model)
if value:
    statement |= where(Model.value == value)
```

## Installation
```shell
$ uv add sqlalchemy-builder
```

or 
```shell
$ pip install sqlalchemy-builder
```

## Why?
There is a common mistake when building sqlalchemy statements.

```py
statement = select(Model)

if status is not None:
    statement.where(Model.status == status)
```
The `statement.where` does not do anything as it generates a new `Select` object.

To fix this we have to assign it:

```py
statement = statement.where(...)
```

This can be a bit verbose though not the worst issue. By using implace `|=` we can avoid this issue without making the statement mutable.

It's also just a fun syntax to play with.

## Development
Installing dependencies:
```bash
$ uv sync 
```

Running tests:
```bash
$ uv run pytest
```
