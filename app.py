from task_manager import TaskManager

def show_menu():
    print("\n==== Task Manager ===")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 完成任务")
    print("4. 退出")

def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("请选择：").strip()

        if choice == "1":
                manager.list_tasks()

        elif choice == "2":
                title = input("请输入任务名称：").strip()

                if not title:
                        print("任务名称不能为空。")
                        continue
           
                priority = input(
                        "请输入优先级(high/medium/low):"
                ).strip().lower()

                if priority not in ["high", "medium", "low"]:
                        print("优先级无效，将使用 medium")
                        priority = "medium"

                manager.add_task(title, priority)

        elif choice == "3":
                manager.list_tasks()

                try:
                        task_number = int(input("请输入要完成的任务编号："))
                        manager.complete_task(task_number)
                except ValueError:
                        print("请输入有效数字。")

        elif choice == "4":
                print("程序已退出。")
                break

        else:
                print("无效选项，请重新输入。")

if __name__ == "__main__":
        main()