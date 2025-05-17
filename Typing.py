from typing import List, Dict, Tuple, Set, Any

# Basic type
def greet(name: str) -> str:
    return f"Hello, {name}!"

age: int = 25
data: Any = "This can be any type"

name: str = "Alice"
age: int = 30
is_active: bool = True

# Container
numbers: List[int] = [1, 2, 3]          # 列表（Python 3.9+ 可直接用 list[int]）
user_info: Dict[str, str] = {"id": "123"}  # 字典（Python 3.9+ 可用 dict[str, str]）
coordinates: Tuple[float, float] = (3.5, 4.2)  # 元组
unique_ids: Set[int] = {1, 2, 3}         # 集合

# Union
from typing import Union
def process(value: Union[int, str]) -> str:
    return str(value)

# Optional (one possible value: None)
from typing import Optional
optional_name: Optional[str] = None      # 等价于 str | None（Python 3.10+）
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None

# Self-defined
from typing import TypeAlias
UserID: TypeAlias = int
def get_user(user_id: UserID) -> str:
    return f"User {user_id}"

# Generic
from typing import TypeVar, Generic, List
T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Callable func.
from typing import Callable

def execute(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = execute(add, 2, 3)