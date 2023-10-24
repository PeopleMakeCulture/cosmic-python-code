# imports - can pycharm add?
from model import Batch


def test_repository_can_save_a_batch(session):
    batch = Batch("batch1", "RUSTY_NAIL", 100, None)