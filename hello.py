"""Git 练习用的最小脚本。"""


def greet(name: str) -> str:
    return f"你好，{name}！"


def farewell(name: str) -> str:
    return f"再见，{name}。"


def shout(name: str) -> str:
    """分支上新增的功能。"""
    return greet(name).upper()


def main() -> None:
    print(shout("分支实验"))


if __name__ == "__main__":
    main()
