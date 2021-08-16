from __future__ import annotations

import math


class Vector:
    """Class of 2D vector objects known from linear algebra"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def add(self, vector: Vector):
        self.x += vector.x
        self.y += vector.y

    def subtract(self, vector: Vector):
        self.x -= vector.x
        self.y -= vector.y

    def multiply(self, scalar: float):
        self.x *= scalar
        self.y *= scalar

    def divide(self, scalar: float):
        self.x /= scalar
        self.y /= scalar

    def reset(self):
        self.x = 0
        self.y = 0

    def magnitude(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def limit(self, limitation: float):
        magnitude = self.magnitude()
        if magnitude != 0 and magnitude > limitation:
            self.x *= limitation / magnitude
            self.y *= limitation / magnitude

    @staticmethod
    def distance(vector1: Vector, vector2: Vector) -> float:
        return math.sqrt(math.pow(vector1.x - vector2.x, 2) + math.pow(vector1.y - vector2.y, 2))

