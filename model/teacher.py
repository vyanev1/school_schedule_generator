from model.time_slot import TimeSlot, days_of_week


class Teacher:
    def __init__(self, name: str, schedule: dict[str, list[TimeSlot]] = None):
        self.name = name
        self.schedule = schedule if schedule else {day: [] for day in days_of_week}

    def occupy(self, day: str, slot: TimeSlot) -> None:
        self.schedule[day].append(slot)
        self.schedule[day].sort(key=lambda s: s.start)

    def has_occupied_slots(self, day: str, start: int = None, end: int = None) -> bool:
        if start >= len(self.schedule[day]):
            return False

        start = max(start, len(self.schedule[day])) if start is not None else 0
        end = max(end, len(self.schedule[day])) if end is not None else len(self.schedule[day])
        return any(not s.is_empty() for s in self.schedule[day][start:end])
