from storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def list_tasks(self):
        """显示所有任务"""
        if not self.tasks:
            print("暂无任务。")
            return
        
        print("\n=== 任务列表 ===")

        for index, task in enumerate(self.tasks, start=1):
            status = "✅" if task["completed"] else " "
            title = task["title"]
            priority = task["priority"]

            print(f"{index}. [{status}] {title} ({priority})")

    def add_task(self, title, priority):
        """添加新任务。"""
        task = {
            "title": title,
            "priority": priority,
            "completed": False,
        }

        self.tasks.append(task)
        save_tasks(self.tasks)

        print("任务添加成功。")

    def complete_task(self, task_number):
        """将指定任务标记为完成。"""
        index = task_number -1

        if index < 0 or index >= len(self.tasks):
            print("任务编号无效。")
            return
        
        self.tasks[index]["completed"] = True
        save_tasks(self.tasks)

        print("任务已完成。")

