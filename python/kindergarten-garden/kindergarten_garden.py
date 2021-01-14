from enum import auto, Enum


class Plant(Enum):
    GRASS = auto()
    CLOVER = auto()
    RADISHES = auto()
    VIOLETS = auto()

    @property
    def title(self):
        return self.name.title()

    @property
    def letter(self):
        return self.name[0]

    @classmethod
    def from_letter(cls, letter: str):
        for plant in Plant:
            if plant.letter == letter:
                return plant


class Garden:
    __DEFAULT_STUDENTS = [
        'Alice',
        'Bob',
        'Charlie',
        'David',
        'Eve',
        'Fred',
        'Ginny',
        'Harriet',
        'Ileana',
        'Joseph',
        'Kincaid',
        'Larry'
    ]

    def __init__(self, diagram: str, students=None):
        diagram_lines = diagram.splitlines()
        if len(diagram_lines) != 2:
            raise ValueError('diagrams must be a two-line string')
        if len(diagram_lines[0]) != len(diagram_lines[1]):
            raise ValueError('First row and second row of diagram must have the same length.')
        self.__first_row = diagram_lines[0]
        self.__second_row = diagram_lines[1]
        self.__students = Garden.__DEFAULT_STUDENTS if students is None else sorted(students)

    def plants(self, student: str):
        student_index = self.__students.index(student)
        return [
            Plant.from_letter(letter).title for letter in [
                self.__first_row[student_index * 2],
                self.__first_row[student_index * 2 + 1],
                self.__second_row[student_index * 2],
                self.__second_row[student_index * 2 + 1]
            ]
        ]
