from typing import List

from model.grade import Grade
from model.subject import Subject
from model.teacher import Teacher
from model.time_slot import TimeSlot, days_of_week


class Schedule:
    def __init__(self, grade: Grade, school_start_time: int, school_end_time: int,
                 class_duration: int, break_duration: int, lunch_break_duration: int):
        self.grade = grade
        self.school_start_time = school_start_time
        self.school_end_time = school_end_time
        self.school_hours = self.school_end_time - self.school_start_time
        self.class_duration = class_duration
        self.break_duration = break_duration
        self.lunch_break_duration = lunch_break_duration
        self.schedule = {
            day: [TimeSlot(day, start * 60, start * 60 + class_duration) for start in range(self.school_hours // class_duration)]
            for day in days_of_week
        }

    def add_class(self, subject: Subject) -> bool:
        day = self.get_least_busy_day()

        time_slot = self.get_next_empty_time_slot(day)
        if time_slot is None:
            return False

        start_time, end_time = time_slot.start, time_slot.end
        start_slot = start_time // self.class_duration
        end_slot = end_time // self.class_duration

        teacher = subject.get_least_busy_teacher(day, start_slot, end_slot)

        subject_classes = [slot for slot in self.get_non_empty_slots(day) if slot.subject_name == subject.name]

        if len(subject_classes) < subject.max_daily_slots:
            self.mark_time_slots_as_occupied(day, start_slot, end_slot, subject, teacher)
            return True
        else:
            return False

    def mark_time_slots_as_occupied(self, day: str, start_slot: int, end_slot: int, subject: Subject, teacher: Teacher):
        start_time = self.get_time_slot_string(self.school_start_time, self.class_duration, start_slot)
        end_time = self.get_time_slot_string(self.school_start_time, self.class_duration, end_slot)
        print(f"Marking {start_time} to {end_time} on {day} as occupied by {(subject.name, teacher.name)}")
        for slot in range(start_slot, end_slot):
            self.schedule[day][slot].occupy(subject.name, teacher.name)
            teacher.occupy(day, self.schedule[day][slot])

    def get_least_busy_day(self) -> str:
        return min(self.schedule.keys(), key=lambda day: len(self.get_non_empty_slots(day)))

    def get_next_empty_time_slot(self, day: str) -> TimeSlot | None:
        return next((slot for slot in self.schedule[day] if slot.is_empty()), None)

    def get_non_empty_slots(self, day: str) -> List[TimeSlot]:
        return [slot for slot in self.schedule[day] if not slot.is_empty()]

    @staticmethod
    def get_time_slot_string(start_time: int, class_duration: int, slot_n: int) -> str:
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
            print(day_of_week, end=" " * (30 - len(day_of_week)))
        print()

        slots_per_day = self.schedule.values()
        max_time_slots = max(map(len, slots_per_day))

        # Rows
        for i in range(0, max_time_slots):
            is_slot_taken_on_any_day = any(i < len(slots) and not slots[i].is_empty() for slots in slots_per_day)
            if not is_slot_taken_on_any_day:
                break

            print(Schedule.get_time_slot_string(self.school_start_time, self.class_duration, i), end=" " * 9)
            for slots in slots_per_day:
                if i < len(slots) and not slots[i].is_empty():
                    subject_str = f"{slots[i].subject_name}: {slots[i].teacher_name}"
                    print(subject_str, end=" " * (30 - len(subject_str)))
            print()
