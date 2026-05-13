import re

def split_words(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?|[\u4e00-\u9fff]", text.casefold())

def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def show_result(counts):
    if not counts:
        print("没有可统计的英文单词或汉字。")
        return
    print("词频统计结果：")
    result = [f"{word}: {count}" for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0]))]
    print(" | ".join(result))

def main():
    try:
        text = input("请输入一段文字: ").strip()
        if not text:
            print("输入不能为空。")
            return
        words = split_words(text)
        counts = count_words(words)
        show_result(counts)
    except Exception as e:
        print(f"输入处理失败，请重试：{e}")

if __name__ == "__main__":
    main()
