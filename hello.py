"""Git 练习用的最小脚本。"""


def greet(name: str) -> str:
    return f"你好，{name}！"


def farewell(name: str) -> str:
    return f"再见，{name}。"


def main() -> None:
    print(greet("世界"))
    print(farewell("世界"))


if __name__ == "__main__":
    main()
