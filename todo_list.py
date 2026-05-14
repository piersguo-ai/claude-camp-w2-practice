import json
from pathlib import Path
FILE_NAME = Path(__file__).with_name("todos.json")

def load_todos():
    try:
        todos = json.loads(FILE_NAME.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    if not isinstance(todos, list): return []
    return [todo for todo in todos if isinstance(todo, dict) and "text" in todo and "done" in todo]

def save_todos(todos):
    FILE_NAME.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")

def show_todos(todos):
    if not todos:
        print("暂无待办事项。"); return
    print("\n待办清单：")
    for index, todo in enumerate(todos, 1):
        status = "完成" if todo["done"] else "未完成"
        print(f"{index}. [{status}] {todo['text']}")

def add_todo(todos):
    text = input("请输入新的待办事项：").strip()
    if not text:
        print("内容不能为空。")
        return
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print("已添加。")

def complete_todo(todos):
    show_todos(todos)
    if not todos: return
    try:
        number = int(input("请输入要完成的编号："))
        if not 1 <= number <= len(todos):
            raise ValueError
    except ValueError:
        print("编号无效。")
        return
    todos[number - 1]["done"] = True
    save_todos(todos)
    print("已标记为完成。")

def main():
    todos = load_todos()
    while True:
        print("\n1. 查看清单\n2. 添加待办\n3. 完成待办\n4. 退出")
        choice = input("请选择操作：").strip()
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            print("再见！")
            break
        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    main()
