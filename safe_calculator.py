import ast


def calculate(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = calculate(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
        left, right = calculate(node.left), calculate(node.right)
        if isinstance(node.op, ast.Add): return left + right
        if isinstance(node.op, ast.Sub): return left - right
        if isinstance(node.op, ast.Mult): return left * right
        if right == 0: raise ZeroDivisionError
        return left / right
    raise ValueError


def main():
    print("安全计算器：输入算式如 1+2/3*5，输入 quit 退出。")
    while True:
        text = input("\n请输入算式：").strip()
        if text.lower() == "quit":
            print("已退出计算器。")
            break
        text = text.rstrip("=").replace("X", "*").replace("x", "*")
        try:
            tree = ast.parse(text, mode="eval")
            print(f"结果：{calculate(tree.body)}")
        except ZeroDivisionError:
            print("除数不能为 0，请重新输入。")
        except (SyntaxError, ValueError, TypeError):
            print("输入无效，请输入数字和 + - * / 组成的算式。")


if __name__ == "__main__":
    main()
