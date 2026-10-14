from models import ExtendedList, ShapeFactory, Student


def main() -> None:
    print("=== Лабораторная работа № 3 (Вариант 2) ===")

    # Задание 2 (средняя): Класс Студент
    print("\n1. Класс «Студент»:")
    alice = Student("Алиса Селезнёва", "ИПМКН-21", 4.88)
    bob = Student("Борис Летов", "ИПМКН-21", 4.62)
    print(alice.display_info())
    print(bob.display_info())

    # Задание 7 (средняя): Перегрузка оператора +
    print("\n2. Перегрузка оператора + (объединение в проект):")
    project_collab = alice + bob
    print(project_collab)


if __name__ == "__main__":
    main()