from .base import Base

class Program(Base):
    """Класс для представления программы обучения"""

    def __init__(self, id = None, code =None, name = None)->None:
        # print("__init__ called")
        super().__init__("program", id, code, name)

    def __del__(self):
        # print("__del__ called")
        pass

    def __str__(self) -> str:
        return f"{self.code}: {self.name}"

    def __repr__(self) -> str:
        return f"{self.code}: {self.name}"
