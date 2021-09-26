
class Base:
    """Базовый класс для многих объектов системы"""
    def __init__(self, type=None, id=None, code=None, name=None):
        self.type = type
        self.id = id or 0
        self.code = code or ""
        self.name = name or ""
