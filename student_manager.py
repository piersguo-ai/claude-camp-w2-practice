from datetime import date

students = {}

def format_date(text):
    try:
        return date.fromisoformat(text).isoformat()
    except ValueError:
        return None

def add_student():
    name = input("姓名: ").strip()
    if not name:
        print("姓名不能为空。")
        return
    email = input("邮箱: ").strip()
    join_date = input("加入日期(YYYY-MM-DD，如 2026-05-14): ").strip()
    if not email or not join_date:
        print("邮箱和加入日期不能为空。")
        return
    join_date = format_date(join_date)
    if not join_date:
        print("日期格式无效，请使用 YYYY-MM-DD，例如 2026-05-14。")
        return
    students[name] = {"邮箱": email, "加入日期": join_date}
    print(f"已添加学员：{name}")

def print_student(name, info):
    print(f"姓名: {name}，邮箱: {info['邮箱']}，加入日期: {info['加入日期']}")

def query_student():
    name = input("请输入要查询的姓名: ").strip()
    info = students.get(name)
    if info:
        print_student(name, info)
    else:
        print("未找到该学员。")

def delete_student():
    name = input("请输入要删除的姓名: ").strip()
    if students.pop(name, None):
        print(f"已删除学员：{name}")
    else:
        print("未找到该学员。")

def show_all():
    if not students:
        print("当前没有学员信息。")
        return
    for name, info in students.items():
        print_student(name, info)

def main():
    actions = {"1": add_student, "2": query_student, "3": delete_student, "4": show_all}
    while True:
        print("\n1.添加 2.查询 3.删除 4.显示全部 5.退出")
        try:
            choice = input("请选择操作: ").strip()
            if choice in actions:
                actions[choice]()
            elif choice == "5":
                print("程序已退出。")
                break
            else:
                print("输入无效，请输入 1 到 5。")
        except Exception as e:
            print(f"输入有误，请重试：{e}")

if __name__ == "__main__": main()
