"""Testing queues."""
from queue1 import Queue


def test_me() -> None:
    """Remember to write tests."""
    assert 40 + 2 == 42


def test_my_code() -> None:
    queue_for_test = Queue()
    assert queue_for_test.is_empty()==True
    to_be_queue = [i for i in range(5,10,2)]
    for i in to_be_queue:
        queue_for_test.enqueue(i)
    assert queue_for_test.front() == to_be_queue[0]
    for i in to_be_queue:
        assert i == queue_for_test.dequeue()


