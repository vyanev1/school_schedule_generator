from typing import List

from constants.schedule_constants import class_duration, school_hours, days_of_week, start_time
from model.grade import Grade
from model.subject import Subject
from model.teacher import Teacher
from model.time_slot import TimeSlot


class Schedule:
    def __init__(self, grade: Grade, schedule: dict[str, list[TimeSlot]] = None):
        self.grade = grade
        self.schedule = schedule if schedule is not None else {
            day: [TimeSlot(day, start * 60, start * 60 + class_duration) for start in range(school_hours // class_duration)]
            for day in days_of_week
        }

    def add_class(self, day: str, subject: Subject) -> bool:
        time_slot = self.get_next_empty_time_slot(day)
        if time_slot is None:
            return False

        start_slot = time_slot.start // class_duration
        end_slot = time_slot.end // class_duration

        teacher = subject.get_least_busy_teacher(day, start_slot, end_slot)
        if teacher is None:
            return False

        subject_classes = [slot for slot in self.schedule[day] if slot.subject_name == subject.name]

        if len(subject_classes) > 0:
            teacher = next(t for t in subject.teachers if t.name == subject_classes[0].teacher_name)
            if teacher.has_occupied_slots(day, start_slot, end_slot):
                return False

        if len(subject_classes) < subject.max_daily_slots:
            self.mark_time_slots_as_occupied(day, start_slot, end_slot, subject, teacher, self.grade)
            return True

        return False

    def mark_time_slots_as_occupied(self, day: str, start_slot: int, end_slot: int,
                                    subject: Subject, teacher: Teacher, grade: Grade):
        start_time_str = self.get_time_slot_string(start_slot)
        end_time_str = self.get_time_slot_string(end_slot)
        print(f"Marking {start_time_str} to {end_time_str} on {day} as occupied by {(subject.name, teacher.name)}")
        for slot in range(start_slot, end_slot):
            self.schedule[day][slot].occupy(grade.grade_number, subject.name, teacher.name)
            teacher.occupy(day, start_slot, end_slot, grade.grade_number, subject.name)

    def get_least_busy_days(self) -> List[str]:
        return sorted(self.schedule.keys(), key=lambda day: len(self.get_non_empty_slots(day)))

    def get_next_empty_time_slot(self, day: str) -> TimeSlot | None:
        return next((slot for slot in self.schedule[day] if slot.is_empty()), None)

    def get_non_empty_slots(self, day: str) -> List[TimeSlot]:
        return [slot for slot in self.schedule[day] if not slot.is_empty()]

    @staticmethod
    def get_time_slot_string(slot_n: int) -> str:
        return Schedule.get_slot_string(start_time + slot_n * class_duration, slot_n * class_duration)

    @staticmethod
    def get_slot_string(start_slot: int, end_slot: int):
        return f"{start_slot // 60:02}:{end_slot % 60:02}"

    def print_schedule(self) -> None:
        # Title
        print(f"\nSchedule for {self.grade.grade_number}th Grade:")

        # Headers
        print("Time", end=" " * 10)
        for day_of_week in self.schedule:
            print(day_of_week, end=" " * (35 - len(day_of_week)))
        print()

        max_time_slots = (
            max(map(len, [list(filter(lambda s: not s.is_empty(), day_slots)) for day_slots in self.schedule.values()])))

        # Rows
        for i in range(0, max_time_slots):
            print(Schedule.get_time_slot_string(i), end=" " * 9)
            for day, slots in self.schedule.items():
                if i < len(slots) and not slots[i].is_empty():
                    subject_str = f"{slots[i].subject_name}: {slots[i].teacher_name}"
                    print(subject_str, end=" " * (35 - len(subject_str)))
            print()
