from constants.schedule_constants import class_duration, days_of_week, school_hours
from model.time_slot import TimeSlot


class Teacher:
    def __init__(self, name: str, schedule: dict[str, list[TimeSlot]] = None):
        self.name = name
        self.schedule = schedule if schedule is not None else {
            day: [TimeSlot(day, start * 60, start * 60 + class_duration) for start in range(school_hours // class_duration)]
            for day in days_of_week
        }

    def occupy(self, day: str, start: int, end: int, grade_number: int, subject_name: str) -> None:
        for i in range(start, end):
            self.schedule[day][i].occupy(grade_number, subject_name, self.name)

    def has_occupied_slots(self, day: str, start: int = None, end: int = None) -> bool:
        start = min(start, len(self.schedule[day])) if start is not None else 0
        end = min(end, len(self.schedule[day])) if end is not None else len(self.schedule[day])
        return any(not s.is_empty() for s in self.schedule[day][start:end])

    def get_occupied_slots(self, day, start: int = None, end: int = None):
        start = min(start, len(self.schedule[day])) if start is not None else 0
        end = min(end, len(self.schedule[day])) if end is not None else len(self.schedule[day])
        return [s for s in self.schedule[day][start:end] if not s.is_empty()]
