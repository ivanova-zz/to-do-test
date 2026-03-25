from typing import List, Optional
from .schemas import Task, TaskCreate, TaskBase

class TaskManager:
    def __init__(self):
        self._tasks: List[Task] = []
        self._current_id = 1

    def get_all(self) -> List[Task]:
        return self._tasks

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return next((t for t in self._tasks if t.id == task_id), None)

    def create(self, task_data: TaskCreate) -> Task:
        new_task = Task(id=self._current_id, **task_data.model_dump())
        self._tasks.append(new_task)
        self._current_id += 1
        return new_task

    def update(self, task_id: int, task_data: TaskBase) -> Optional[Task]:
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                updated_task = Task(id=task_id, **task_data.model_dump())
                self._tasks[i] = updated_task
                return updated_task
        return None

    def delete(self, task_id: int) -> bool:
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                self._tasks.pop(i)
                return True
        return False

task_service = TaskManager()