
# place super_test.py code here


class Character:
    def __init__(self, speed: int =2, jump: int=2, power: int=2) -> None:
        self._speed = speed
        self._jump = jump
        self._power = power

    def jump(self) -> int:
        return self._jump

    def speed(self) -> int:
        return self._speed

    def power(self) -> int:
        return self._power


class Mario(Character):
    def speed(self) -> int:
        parent = super().speed()
        return parent + 2


class Luigi(Character):
    def speed(self) -> int:
        parent = super().speed()
        return parent + 1


# place keyword_test.py code here

def force(*, mass: int, acceleration: int) -> float:
    return mass * acceleration

