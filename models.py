from abc import ABC, abstractmethod
import math
from typing import List


class Student:
    """Сущность студента с академическими данными."""

    def __init__(self, full_name: str, group_code: str, rating: float) -> None:
        self.full_name = full_name
        self.group_code = group_code
        self.rating = rating

    def display_info(self) -> str:
        """Формирует строковое представление сведений об учащемся."""
        return (
            f"Обучающийся: {self.full_name} | "
            f"Группа: {self.group_code} | "
            f"Успеваемость: {self.rating:.2f}"
        )

    def __add__(self, other: object) -> "StudentGroup":
        """Объединение двух студентов в совместную проектную ячейку."""
        if not isinstance(other, Student):
            return NotImplemented
        avg_rating = (self.rating + other.rating) / 2
        return StudentGroup(
            members=[self.full_name, other.full_name],
            collective_rating=avg_rating,
        )


class StudentGroup:
    """Проектная группа, полученная путем сложения студентов."""

    def __init__(self, members: List[str], collective_rating: float) -> None:
        self.members = members
        self.collective_rating = collective_rating

    def __str__(self) -> str:
        names = " & ".join(self.members)
        return (
            f"Команда [{names}], средний рейтинг: "
            f"{self.collective_rating:.2f}"
        )