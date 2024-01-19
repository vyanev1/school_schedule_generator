from typing import List


class Subject:
    MAX_DAILY_SLOTS = 2

    def __init__(self, name: str, teachers: List[str], classes_per_week: int, max_daily_slots: int = MAX_DAILY_SLOTS):
        self.name = name
        self.teachers = teachers
        self.classes_per_week = classes_per_week
        self.max_daily_slots = max_daily_slots
