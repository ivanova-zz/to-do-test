import pytest
from pydantic import ValidationError
from app.schemas import TaskCreate, Task


def test_task_create_valid():
    data = {"title": "Test Task"}
    task = TaskCreate(**data)
    assert task.title == "Test Task"
    assert task.status == "TODO"
    assert task.description is None

def test_task_create_invalid_title():
    with pytest.raises(ValidationError):
        TaskCreate(description="No title here")

def test_task_create_wrong_type():
    with pytest.raises(ValidationError):
        TaskCreate(title={"key": "value"})

def test_task_output_logic():
    data = {
        "id": 1,
        "title": "Complete Task",
        "description": "Done it!",
        "status": "DONE"
    }
    task = Task(**data)
    assert task.id == 1
    assert task.status == "DONE"

def test_task_missing_id():
    with pytest.raises(ValidationError):
        Task(title="Needs ID")