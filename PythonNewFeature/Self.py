from typing import Self

class Animal:
    def __init__(self, name: str):
        self.name = name

    def clone(self) -> Self:  # 返回类型是当前类或其子类
        return type(self)(self.name)

    def bark(self) -> str:
        return "Woof!"

# 类型检查会正确推断 dog.clone() 返回 Dog 类型
dog = Dog("Buddy")
cloned_dog = dog.clone()
cloned_dog.bark()  # 类型检查通过，知道 cloned_dog 是 Dog 实例
