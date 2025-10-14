from models.task import Task

class TaskController:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description=""):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return self.tasks

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False