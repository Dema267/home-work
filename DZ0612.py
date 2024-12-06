#Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description  # Описание задачи
        self.deadline = deadline          # Срок выполнения
        self.completed = False            # Статус выполнения (по умолчанию - не выполнено)

    def mark_completed(self):
        self.completed = True             # Отметить задачу как выполненную

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (Срок: {self.deadline}, Статус: {status})"

class TaskManager:
    def __init__(self):
        self.tasks = []                   # Список задач

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)  # Создание новой задачи
        self.tasks.append(new_task)            # Добавление задачи в список

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()  # Отметка задачи как выполненной
        else:
            print("Неверный индекс задачи.")

    def show_current_tasks(self):
        print("Текущие задачи (не выполненные):")
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{i + 1}. {task}")  # Вывод текущих задач


# Пример использования
if __name__ == "__main__":
    task_manager = TaskManager()

    # Добавление задач
    task_manager.add_task("Сделать домашнее задание по программированию от Zerocoder", "2024-06-12")
    task_manager.add_task("Купить машину", "2025-06-01")
    task_manager.add_task("Пойти в поликлинику и сделать МРТ плеча", "2025-06-02")

    # Показать текущие задачи
    task_manager.show_current_tasks()

    # Отметка задачи как выполненной
    task_manager.mark_task_completed(1)  # Отметить вторую задачу как выполненную

    # Показать текущие задачи снова
    task_manager.show_current_tasks()