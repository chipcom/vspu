from .base import Base
# import DB

class Program(Base):
    """Класс для представления программы обучения"""

    level = ["балаквариат", "магистратура", "специалитет"]

    def __init__(self, id = None, code =None, name = None, level = None)->None:
        # print("__init__ called")
        super().__init__("program", id, code, name)
        self.level = level or 0

    def __del__(self):
        # print("__del__ called")
        pass

    def __str__(self) -> str:
        return f"{self.code}: {self.name}, уровень: {Program.level[self.level]}"

    def __repr__(self) -> str:
        return f"{self.code}: {self.name}, уровень: {Program.level[self.level]}"
    
