"""Git 练习用的最小脚本。"""

import sys


def greet(name: str) -> str:
    return f"你好，{name}！"


def farewell(name: str) -> str:
    return f"再见，{name}。"


def shout(name: str) -> str:
    """把问候语转成大写。"""
    return greet(name).upper()


def resolve_name(argv: list[str]) -> str:
    """有参数就用参数，没有就回退到默认值。"""
    return argv[1] if len(argv) > 1 else "世界"


def main() -> None:
    print(shout(resolve_name(sys.argv)))


if __name__ == "__main__":
    main()
