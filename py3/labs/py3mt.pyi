def force(*, mass: float, acceleration: float) -> float: ...


class Character:
    def __init__(self, speed: int = 2, jump: int = 2, power: int = 2) -> None: ...
    def speed(self) -> int: ...


class Mario:
    def speed(self) -> int: ...
