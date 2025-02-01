"""Sqlalchemy `Select` methods redefined statically.

The documentation and functionality is the same as `Select` methods from sqlalchemy. But here they
are used statically and supports `|` and `|=` operators.

```py
from sqlalchemy_builder import select, where, order_by

stmt = select(MyModel) | where(MyModel.x == 1)
stmt |= order_by(MyModel.id)
```

The following sqlalchemy operations are available:

- [where](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.where)
- [join](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.join)
- [filter](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.filter)
- [filter_by](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.filter_by)
- [having](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.having)
- [group_by](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.group_by)
- [order_by](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.order_by)
- [offset](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.offset)
- [limit](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.limit)
- [add_cte](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.add_cte)
- [options](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.options)
- [execution_options](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.execution_options)
- [outerjoin](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.outerjoin)
- [join_from](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.join_from)
- [outerjoin_from](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.outerjoin_from)
- [distinct](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.distinct)
- [correlate](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.correlate)
- [correlate_except](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.Select.correlate_except)
"""

from sqlalchemy import Select, select

from ._functional import curry_and_swap

__all__ = (
    "select",
    "where",
    "join",
    "filter",
    "filter_by",
    "having",
    "group_by",
    "order_by",
    "offset",
    "limit",
    "add_cte",
    "options",
    "execution_options",
    "outerjoin",
    "join_from",
    "outerjoin_from",
    "distinct",
    "correlate",
    "correlate_except",
)


__pdoc__ = {s: False for s in __all__}  # Turn off documentation for now


where = curry_and_swap(Select.where)
join = curry_and_swap(Select.join)
filter = curry_and_swap(Select.filter)
filter_by = curry_and_swap(Select.filter_by)
having = curry_and_swap(Select.having)
group_by = curry_and_swap(Select.group_by)
order_by = curry_and_swap(Select.order_by)
offset = curry_and_swap(Select.offset)
limit = curry_and_swap(Select.limit)
add_cte = curry_and_swap(Select.add_cte)
options = curry_and_swap(Select.options)
execution_options = curry_and_swap(Select.execution_options)
outerjoin = curry_and_swap(Select.outerjoin)
join_from = curry_and_swap(Select.join_from)
outerjoin_from = curry_and_swap(Select.outerjoin_from)
distinct = curry_and_swap(Select.distinct)
correlate = curry_and_swap(Select.correlate)
correlate_except = curry_and_swap(Select.correlate_except)
