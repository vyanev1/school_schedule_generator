import random
from typing import List

import names

from model.grade import Grade
from model.schedule import Schedule
from model.subject import Subject
from model.teacher import Teacher


def schedule_classes(schedules: List[Schedule]) -> None:
    n_tries = 0
    success = False

    while not success:
        try:
            n_tries += 1
            random.seed(random.randint(1, 100_000))

            for schedule in schedules:
                for day in schedule.schedule:
                    for slot in schedule.schedule[day]:
                        slot.mark_as_empty()
                for teacher in list(t for subject in schedule.grade.subjects for t in subject.teachers):
                    for day in teacher.schedule:
                        for slot in teacher.schedule[day]:
                            slot.mark_as_empty()

            for schedule in schedules:
                # print(f"\nScheduling classes for {schedule.grade.grade_number}th Grade:")
                for subject in schedule.grade.subjects:
                    for i in range(subject.classes_per_week):
                        class_scheduled = False

                        days_shuffled = schedule.get_least_busy_days()
                        random.shuffle(days_shuffled)

                        for day in days_shuffled:
                            if schedule.add_class(day, subject):
                                class_scheduled = True
                                break

                        if not class_scheduled:
                            raise ValueError(f"Could not schedule class of {subject.name} "
                                            f"for {schedule.grade.grade_number}th Grade. "
                                            f"Consider adding more teachers!")
            else:
                success = True
        except ValueError:
            if n_tries >= 1_000_000:
                raise Exception("Scheduling failed!")


def main():
    teachers = [Teacher(names.get_full_name()) for _ in range(30)]

    subjects = [
        Subject(name="Literature", teachers=teachers[0:3], classes_per_week=3, max_daily_slots=2),
        Subject(name="Math", teachers=teachers[3:6], classes_per_week=3, max_daily_slots=2),
        Subject(name="English", teachers=teachers[6:11], classes_per_week=4, max_daily_slots=2),
        Subject(name="German", teachers=teachers[11:14], classes_per_week=3, max_daily_slots=2),
        Subject(name="Biology", teachers=teachers[14:16], classes_per_week=2, max_daily_slots=2),
        Subject(name="Chemistry", teachers=teachers[16:18], classes_per_week=2, max_daily_slots=2),
        Subject(name="Physics", teachers=teachers[18:20], classes_per_week=2, max_daily_slots=2),
        Subject(name="Geography", teachers=teachers[20:22], classes_per_week=2, max_daily_slots=2),
        Subject(name="History", teachers=teachers[22:24], classes_per_week=2, max_daily_slots=2),
        Subject(name="Physical Ed", teachers=teachers[24:26], classes_per_week=2, max_daily_slots=1),
        Subject(name="Philosophy", teachers=teachers[26:28], classes_per_week=2, max_daily_slots=1),
        Subject(name="Informatics", teachers=teachers[28:30], classes_per_week=2, max_daily_slots=1),
    ]

    # Create Schedule instances for each different Grade
    grade_schedules = []
    for grade_number in range(8, 13):
        grade = Grade(grade_number, subjects)
        grade_schedules.append(Schedule(grade))

    # Generate schedule
    schedule_classes(grade_schedules)

    for grade_schedule in grade_schedules:
        grade_schedule.print_schedule()


if __name__ == "__main__":
    main()
