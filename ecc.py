from typing import Union


class Curve:
    """Elliptic Curves of Weierstrass normal form y ** 2 = x ** 3 + a * x + b
    in finite fields.
    """
    def __init__(self, a: int, b: int, p: int, name: str) -> None:
        self.a = a
        self.b = b
        self.p = p
        self.name = name
        assert not self.is_singular()

    def is_singular(self) -> bool:
        return (4 * self.a ** 3 + 27 * self.b ** 2) % self.p == 0

    def __eq__(self, other: "Curve") -> bool:
        if isinstance(other, Curve):
            return self.a == other.a and self.b == other.b \
                and self.p == other.p and self.name == other.name
        return False

    def on_curve(self, x: int, y: int) -> bool:
        return (y ** 2 - x ** 3 - self.a * x - self.b) % self.p == 0

    def __str__(self) -> str:
        return f'y ** 2 = x ** 3 + {self.a}x + {self.b}'


class SubGroup:
    def __init__(self, ):
        pass


class Point:
    """Point manipulation on a finite fileds over an elliptic curve.
    """
    def __init__(self, curve: Curve, x: int, y: int) -> None:
        self.curve = curve
        self.x = x
        self.y = y
        assert self.curve.on_curve(x, y), f"point ({x},{y}) not on curve {curve}"

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y and self.curve == other.curve

    def __add__(self, other: Union["Point", "Inf"]) -> "Point":
        assert self.curve == other.curve, (
            f"Must use the same curve, found{self.curve} and {other.curve}")
        if isinstance(other, Inf):
            # a + 0 = a
            return self
        else:
            pass

    def __neg__(self) -> "Point":
        # Q + (-Q) = 0. Vertical line.
        return Point(curve=self.curve, x=self.x, y=(-self.y) % self.curve.p)


class Inf:
    def __init__(self, curve: Curve) -> None:
        self.curve = curve
