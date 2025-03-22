from schemas import TaskCreate, TaskGet


class DB:

    def __init__(self):
        self.storage: dict[int, TaskGet] = {}
        self.max_id: int = 1

    def add(self, task: TaskCreate) -> int:
        """
        Создает задачу, возвращает ID созданной задачи
        """
        new_task = TaskGet(
            id=self.max_id,
            **task.model_dump(),
        )
        self.storage[new_task.id] = new_task
        self.max_id += 1
        return new_task.id

    def get_all(self) -> list[TaskGet]:
        """
        Получить список всех задач
        """
        return list(self.storage.values())

    def delete(self, task_id: int) -> bool:
        """
        Удалить задачу по ID

        Если задача не удалена возвращает False, если удалена - True
        """
        return bool(
            self.storage.pop(task_id, False),
        )


db = DB()
