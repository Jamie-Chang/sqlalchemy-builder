import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from sqlalchemy_builder.select import where


class Base(DeclarativeBase):
    pass  # Inherit from this to define declarative models


class Model(Base):
    __tablename__ = "model"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()


@pytest.fixture(scope="module")
def engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        model1 = Model(value="test1", status="active")
        model2 = Model(value="test2", status="inactive")
        model3 = Model(value="test3", status="active")
        session.add_all([model1, model2, model3])
        yield session
    finally:
        session.rollback()
        session.close()


def test_basic_select(session):
    stmt = select(Model) | where(Model.id == 1)
    results = session.execute(stmt).scalars().all()
    assert len(results) == 1
    assert results[0].value == "test1"


def test_chained_where(session):
    stmt = select(Model) | where(Model.id == 1) | where(Model.value == "test1")
    results = session.execute(stmt).scalars().all()
    assert len(results) == 1
    assert results[0].value == "test1"

    stmt = select(Model) | where(Model.id == 1) | where(Model.value == "test2")
    results = session.execute(stmt).scalars().all()
    assert len(results) == 0


def test_inplace_where(session):
    stmt = select(Model)
    value = "test2"
    stmt |= where(Model.value == value)
    results = session.execute(stmt).scalars().all()
    assert len(results) == 1
    assert results[0].value == "test2"


def test_conditional_where(session):
    stmt = select(Model)
    status = "active"
    if status:
        stmt |= where(Model.status == status)

    results = session.execute(stmt).scalars().all()
    assert len(results) == 2

    status = None
    stmt = select(Model)
    if status:
        stmt |= where(Model.status == status)
    results = session.execute(stmt).scalars().all()
    assert len(results) == 3


def test_empty_where(session):
    stmt = select(Model) | where()
    results = session.execute(stmt).scalars().all()
    assert len(results) == 3


def test_no_where_clause(session):
    stmt = select(Model)
    results = session.execute(stmt).scalars().all()
    assert len(results) == 3


def test_where_clause_with_no_conditions(session):
    stmt = select(Model) | where()
    results = session.execute(stmt).scalars().all()
    assert len(results) == 3
