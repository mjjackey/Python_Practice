from typing import Literal

# 只允许 "GET" 或 "POST"
HttpMethod = Literal["GET", "POST"]
def request(method: HttpMethod, url: str) -> None:
    print(f"{method} {url}")

request("GET", "/api")  # 通过
request("DELETE", "/api")  # Terminal Use 'mypy Literal.py' to check type

# 结合 Union 使用
Mode = Literal["read", "write"]
def open_file(mode: Mode) -> None: ...

# 动态生成字面量类型（Python 3.11+）
ALLOWED_COLORS = ("red", "green", "blue")
Color = Literal[*ALLOWED_COLORS]  # 展开为 Literal["red", "green", "blue"]

