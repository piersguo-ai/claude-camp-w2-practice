students = {}

def add_student():
    name = input("姓名: ").strip()
    if not name:
        print("姓名不能为空。"); return
    students[name] = {
        "邮箱": input("邮箱: ").strip(),
        "加入日期": input("加入日期(如 2026-05-13): ").strip()
    }
    print(f"已添加学员：{name}")

def query_student():
    name = input("请输入要查询的姓名: ").strip()
    info = students.get(name)
    print(f"姓名: {name}，邮箱: {info['邮箱']}，加入日期: {info['加入日期']}") if info else print("未找到该学员。")

def delete_student():
    name = input("请输入要删除的姓名: ").strip()
    print(f"已删除学员：{name}") if students.pop(name, None) else print("未找到该学员。")

def show_all():
    if not students:
        print("当前没有学员信息。"); return
    for name, info in students.items():
        print(f"姓名: {name}，邮箱: {info['邮箱']}，加入日期: {info['加入日期']}")

while True:
    print("\n1.添加 2.查询 3.删除 4.显示全部 5.退出")
    try:
        choice = input("请选择操作: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            query_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            show_all()
        elif choice == "5":
            print("程序已退出。"); break
        else:
            print("输入无效，请输入 1 到 5。")
    except Exception as e:
        print(f"输入有误，请重试：{e}")
