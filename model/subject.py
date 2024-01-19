from typing import List

from model.teacher import Teacher


class Subject:
    MAX_DAILY_SLOTS = 2

    def __init__(self, name: str, teachers: List[Teacher], classes_per_week: int, max_daily_slots: int = MAX_DAILY_SLOTS):
        self.name = name
        self.teachers = teachers
        self.classes_per_week = classes_per_week
        self.max_daily_slots = max_daily_slots

    def get_least_busy_teacher(self, day: str, start: int = None, end: int = None) -> Teacher:
        available_teachers = [t for t in self.teachers if not t.has_occupied_slots(day, start, end)]
        return min(available_teachers, key=lambda t: len(t.schedule[day]))
