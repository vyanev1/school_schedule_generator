from typing import List, Tuple

from grade import Grade
from subject import Subject


class Schedule:
    def __init__(self, grade: Grade, days_of_week: List[str], school_start_time: int, school_end_time: int,
                 class_duration: int, break_duration: int, lunch_break_duration: int):
        self.grade = grade
        self.school_start_time = school_start_time
        self.school_end_time = school_end_time
        self.school_hours = self.school_end_time - self.school_start_time
        self.class_duration = class_duration
        self.days_of_week = days_of_week
        self.break_duration = break_duration
        self.lunch_break_duration = lunch_break_duration
        self.schedule = {
            day: [{"subject": None, "teacher": None} for _ in range(self.school_hours // self.class_duration)] for day in days_of_week}

    def add_class(self, subject: Subject) -> bool:
        day = self.get_least_busy_day()
        teacher = self.get_least_busy_teacher(day, subject.teachers)

        time_slot = self.get_next_empty_time_slot(day)
        if time_slot is None:
            return False

        start_time, end_time = time_slot
        start_slot = start_time // self.class_duration
        end_slot = end_time // self.class_duration

        all_taken_slots_for_day = self.get_non_empty_slots(day)
        subject_classes = list(filter(lambda slot: slot["subject"] == subject.name, all_taken_slots_for_day))

        if len(subject_classes) < subject.max_daily_slots:
            self.mark_time_slots_as_occupied(day, start_slot, end_slot, subject, teacher)
            return True
        else:
            return False

    def mark_time_slots_as_occupied(self, day: str, start_slot: int, end_slot: int, subject: Subject, teacher: str):
        start_time = self.get_time_slot_string(self.school_start_time, self.class_duration, start_slot)
        end_time = self.get_time_slot_string(self.school_start_time, self.class_duration, end_slot)
        print(f"Marking {start_time}:{end_time} on {day} as occupied by {(subject.name, teacher)}")
        for slot in range(start_slot, end_slot):
            self.schedule[day][slot]["subject"] = subject.name
            self.schedule[day][slot]["teacher"] = teacher

    def get_least_busy_day(self) -> str:
        return min(self.schedule.keys(), key=lambda day: len(self.get_non_empty_slots(day)))

    def get_least_busy_teacher(self, day: str, teachers: List[str]) -> str:
        all_taken_slots_for_day = self.get_non_empty_slots(day)
        return min(teachers, key=lambda teacher: len([slot for slot in all_taken_slots_for_day if slot["teacher"] == teacher]))

    def get_next_empty_time_slot(self, day: str) -> Tuple[int, int] | None:
        empty_slot = next((index for index, slot in enumerate(self.schedule[day]) if slot["subject"] is None), None)
        if empty_slot is None:
            return None
        else:
            start_time = empty_slot * 60
            end_time = start_time + self.class_duration
            return start_time, end_time

    def get_non_empty_slots(self, day: str):
        return list(filter(lambda slot: slot["subject"] is not None, self.schedule[day]))

    @staticmethod
    def get_time_slot_string(start_time: int, class_duration: int, slot_n: int) -> str:
        return Schedule.get_slot_string(start_time + slot_n * class_duration, slot_n * class_duration)

    @staticmethod
    def get_slot_string(start_slot: int, end_slot: int):
        return f"{start_slot // 60:02}:{end_slot % 60:02}"