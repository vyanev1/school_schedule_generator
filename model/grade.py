from typing import List

from model.subject import Subject


class Grade:
    def __init__(self, grade_number: int, subjects: List[Subject]):
        self.grade_number = grade_number
        self.subjects = subjects
