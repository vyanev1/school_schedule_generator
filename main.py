import random
from typing import List

from grade import Grade
from schedule import Schedule
from schedule_factory import ScheduleFactory
from subject import Subject


def schedule_classes(schedules: List[Schedule]) -> None:
    for schedule in schedules:
        print(f"\nScheduling classes for {schedule.grade.grade_number}th Grade:")
        for subject in schedule.grade.subjects:
            for _ in range(subject.classes_per_week):
                success = False
                while not success:
                    success = schedule.add_class(subject)


def print_schedule(s: Schedule) -> None:
    # Title
    print(f"\nSchedule for {s.grade.grade_number}th Grade:")

    # Headers
    print("Time", end=" " * 10)
    for day_of_week in s.schedule:
        print(day_of_week, end=" " * (30 - len(day_of_week)))

    print()

    slots_per_day = s.schedule.values()
    max_time_slots = max(map(len, slots_per_day))

    for i in range(0, max_time_slots):
        is_time_range_taken = any(map(lambda slots: i < len(slots) and slots[i]['subject'] is not None, slots_per_day))
        if not is_time_range_taken:
            break

        time_slot: str = Schedule.get_time_slot_string(s.school_start_time, s.class_duration, i)
        print(time_slot, end=" " * 9)
        for slots in slots_per_day:
            if i < len(slots) and slots[i]['subject'] is not None and slots[i]['teacher'] is not None:
                subject_str = f"{slots[i]['subject']}: {slots[i]['teacher']}"
                print(subject_str, end=" " * (30 - len(subject_str)))
        print()


if __name__ == "__main__":
    # Create Grade instances with subjects data
    eighth_grade = Grade(8, subjects=[
        Subject(name="Literature", teachers=["Teacher1", "Teacher2"], classes_per_week=3, max_daily_slots=1),
        Subject(name="Math", teachers=["Teacher3", "Teacher4"], classes_per_week=3, max_daily_slots=1),
        Subject(name="English", teachers=["Teacher5", "Teacher6", "Teacher7"],  classes_per_week=5, max_daily_slots=2),
        Subject(name="German", teachers=["Teacher8", "Teacher9"], classes_per_week=3, max_daily_slots=1),
        Subject(name="Biology", teachers=["Teacher10", "Teacher11"], classes_per_week=2, max_daily_slots=1),
        Subject(name="Chemistry", teachers=["Teacher12"], classes_per_week=2, max_daily_slots=1),
        Subject(name="Physics", teachers=["Teacher13"], classes_per_week=2, max_daily_slots=1),
        Subject(name="Geography", teachers=["Teacher14"], classes_per_week=2, max_daily_slots=1)
    ])
    eighth_grade_schedule = ScheduleFactory.create_schedule(eighth_grade)

    ninth_grade = Grade(9, subjects=[
        Subject(name="Literature", teachers=["Teacher1", "Teacher2"], classes_per_week=3, max_daily_slots=1),
        Subject(name="Math", teachers=["Teacher3", "Teacher4"], classes_per_week=3, max_daily_slots=1),
        Subject(name="English", teachers=["Teacher5", "Teacher6", "Teacher7"],  classes_per_week=4, max_daily_slots=2),
        Subject(name="German", teachers=["Teacher8", "Teacher9"], classes_per_week=3, max_daily_slots=1),
        Subject(name="Biology", teachers=["Teacher10", "Teacher11"], classes_per_week=2, max_daily_slots=1),
        Subject(name="Chemistry", teachers=["Teacher12"], classes_per_week=2, max_daily_slots=1),
        Subject(name="Physics", teachers=["Teacher13"], classes_per_week=2, max_daily_slots=1),
        Subject(name="Geography", teachers=["Teacher14"], classes_per_week=2, max_daily_slots=1)
    ])
    ninth_grade_schedule = ScheduleFactory.create_schedule(ninth_grade)

    # Generate schedule
    grade_schedules = [eighth_grade_schedule, ninth_grade_schedule]
    schedule_classes(grade_schedules)

    for s in grade_schedules:
        print_schedule(s)
