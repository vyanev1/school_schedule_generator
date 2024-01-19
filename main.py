from typing import List

from model.grade import Grade
from model.schedule import Schedule
from factory.schedule_factory import ScheduleFactory
from model.subject import Subject
from model.teacher import Teacher


def schedule_classes(schedules: List[Schedule]) -> None:
    for schedule in schedules:
        print(f"\nScheduling classes for {schedule.grade.grade_number}th Grade:")
        for subject in schedule.grade.subjects:
            for _ in range(subject.classes_per_week):
                success = False
                while not success:
                    success = schedule.add_class(subject)


if __name__ == "__main__":
    # Create Grade instances with subjects data
    teachers = [Teacher(f"Teacher{i}") for i in range(1, 15)]

    eighth_grade = Grade(8, subjects=[
        Subject(name="Literature", teachers=teachers[0:2], classes_per_week=3, max_daily_slots=1),
        Subject(name="Math", teachers=teachers[2:4], classes_per_week=3, max_daily_slots=1),
        Subject(name="English", teachers=teachers[4:7],  classes_per_week=5, max_daily_slots=2),
        Subject(name="German", teachers=teachers[7:9], classes_per_week=3, max_daily_slots=1),
        Subject(name="Biology", teachers=teachers[9:11], classes_per_week=2, max_daily_slots=1),
        Subject(name="Chemistry", teachers=teachers[11:12], classes_per_week=2, max_daily_slots=1),
        Subject(name="Physics", teachers=teachers[12:13], classes_per_week=2, max_daily_slots=1),
        Subject(name="Geography", teachers=teachers[13:14], classes_per_week=2, max_daily_slots=1)
    ])
    eighth_grade_schedule = ScheduleFactory.create_schedule(eighth_grade)

    ninth_grade = Grade(9, subjects=[
        Subject(name="Literature", teachers=teachers[0:2], classes_per_week=3, max_daily_slots=1),
        Subject(name="Math", teachers=teachers[2:4], classes_per_week=3, max_daily_slots=1),
        Subject(name="English", teachers=teachers[4:7],  classes_per_week=5, max_daily_slots=2),
        Subject(name="German", teachers=teachers[7:9], classes_per_week=3, max_daily_slots=1),
        Subject(name="Biology", teachers=teachers[9:11], classes_per_week=2, max_daily_slots=1),
        Subject(name="Chemistry", teachers=teachers[11:12], classes_per_week=2, max_daily_slots=1),
        Subject(name="Physics", teachers=teachers[12:13], classes_per_week=2, max_daily_slots=1),
        Subject(name="Geography", teachers=teachers[13:14], classes_per_week=2, max_daily_slots=1)
    ])
    ninth_grade_schedule = ScheduleFactory.create_schedule(ninth_grade)

    # Generate schedule
    grade_schedules = [eighth_grade_schedule, ninth_grade_schedule]
    schedule_classes(grade_schedules)

    for grade_schedule in grade_schedules:
        grade_schedule.print_schedule()
