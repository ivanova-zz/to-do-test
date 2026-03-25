import pytest
from app.manager import TaskManager
from app.schemas import TaskCreate, TaskBase


@pytest.fixture
def manager():
    return TaskManager()


def test_create_task(manager):
    data = TaskCreate(title="Logic Test", description="Testing manager")
    task = manager.create(data)

    assert task.id == 1
    assert task.title == "Logic Test"
    assert len(manager.get_all()) == 1


def test_get_by_id(manager):
    manager.create(TaskCreate(title="Find me"))
    task = manager.get_by_id(1)
    assert task is not None
    assert task.title == "Find me"


def test_update_task(manager):
    manager.create(TaskCreate(title="Old"))
    update_data = TaskBase(title="New", status="DONE")

    updated = manager.update(1, update_data)
    assert updated.title == "New"
    assert updated.status == "DONE"


def test_delete_task(manager):
    manager.create(TaskCreate(title="Delete me"))
    assert manager.delete(1) is True
    assert len(manager.get_all()) == 0

def test_create_and_get_all(manager):
    manager.create(TaskCreate(title="Task 1"))
    manager.create(TaskCreate(title="Task 2"))
    assert len(manager.get_all()) == 2


def test_get_by_id_not_found(manager):
    task = manager.get_by_id(999)
    assert task is None


def test_update_task_not_found(manager):
    update_data = TaskBase(title="New Title")
    result = manager.update(999, update_data)
    assert result is None


def test_delete_task_not_found(manager):
    result = manager.delete(999)
    assert result is False


def test_id_incrementation(manager):
    t1 = manager.create(TaskCreate(title="First"))
    manager.delete(t1.id)
    t2 = manager.create(TaskCreate(title="Second"))

    assert t1.id == 1
    assert t2.id == 2  # Счетчик не должен откатываться назад
    assert len(manager.get_all()) == 1


def test_update_preserves_id(manager):
    task = manager.create(TaskCreate(title="Original"))
    original_id = task.id

    updated = manager.update(original_id, TaskBase(title="Updated"))
    assert updated.id == original_id