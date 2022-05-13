from datetime import date
from model import Batch, OrderLine


def test_allocating_to_a_batch_reduces_the_available_quantity():
    # Create a batch with a qty of 20
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    # Create a order line to allocate 2 units
    line = OrderLine('order-ref', "SMALL-TABLE", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18


def test_if_stock_is_avalable_to_allocate():
    # Create a batch with a qty of 20
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    # Create an order that requests more stock than avalable
    line = OrderLine('order-ref', "SMALL-TABLE", 22)

    batch.allocate(line)

    # assert that the batch hasn't processed
    assert batch.available_quantity == 20


'''
def test_if_orderline_can_be_duplicated():
    # Create a batch with a qty of 20
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    # Create a order line to allocate 2 units
    line = OrderLine('order-ref', "SMALL-TABLE", 2)

    # allocate inventory once
    batch.allocate(line)
    # attempt to allocate inventory a second time
    batch.allocate(line)

    assert batch.available_quantity == 18
'''
