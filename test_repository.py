# imports - can pycharm add?
from repository import SqlAlchemyRepository
from model import Batch, OrderLine

# import session - not needed - WHY? BC session is coming from pytest not SA


def test_repository_can_save_a_batch(session):
    batch = Batch("batch1", "RUSTY_NAIL", 100, eta=None)
    repo = SqlAlchemyRepository(session)  # see repository.py
    repo.add(batch)
    session.commit()

    rows = session.execute(
        'SELECT reference, sku, _purchased_quantity, eta FROM "batches"'
    )

    assert list(rows) == [("batch1", "RUSTY_NAIL", 100, None)]


def insert_order_line(session):
    session.execute(
        "INSERT INTO order_lines (orderid, sku, qty)" ' VALUES ("order1", "SOFA", 12)'
    )
    [[orderline_id]] = session.execute(
        "SELECT id FROM order_lines WHERE orderid=:orderid AND sku=:sku",
        dict(orderid="order1", sku="SOFA"),
    )
    return orderline_id


# creates a couple batches
def insert_batch(session, batch_id):
    # TODO
    return batch_id


# allocate an order line to a batch
def insert_allocation(session, orderline_id, batch_id):
    # TODO
    pass


def test_repository_can_retrieve_a_batch_with_allocations(session):
    # create some order lines and batches, and allocate one order line to a batch
    orderline_id = insert_order_line(session)
    batch1_id = insert_batch(session, "batch1")
    insert_batch(session, "batch2")
    insert_allocation(session, orderline_id, batch1_id)

    # create repository
    repo = SqlAlchemyRepository(session)
    retrieved = repo.get("batch1")

    expected = Batch("batch1", "SOFA", 100, eta=None)
    assert retrieved == expected
    assert retrieved.sku == expected.sku
    assert retrieved._purchased_quantity == expected._purchased_quantity
    assert retrieved._allocations == {OrderLine("order1", "SOFA", 12)}
