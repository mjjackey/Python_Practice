from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str | None  # Optional

user: User = {"name": "Alice", "age": 30} # Missing key "email" for TypedDict "User"

# Not Required
from typing import NotRequired

class User(TypedDict):
    name: str
    age: NotRequired[int]  # 可选键

user: User = {"name": "Alice"}  # age 可以省略

#Or use total=False
class User(TypedDict, total=False):
    name: str
    age: int

#Inherit
class BaseUser(TypedDict):
    name: str

class AdminUser(BaseUser):
    admin_level: int

admin: AdminUser = {"name": "Alice", "admin_level": 5}

#Dynamic type checking
class User(TypedDict):
    name: str
    age: int

user = {"name": "Alice", "age": 30}
print(isinstance(user, dict))  # True，但不能直接检查 TypedDict 类型