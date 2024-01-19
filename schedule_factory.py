from grade import Grade
from schedule import Schedule


class ScheduleFactory:

    @staticmethod
    def create_schedule(grade: Grade) -> Schedule:
        # Define days of the week
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        # Define class duration, break duration, and lunch break duration in minutes
        class_duration = 60
        break_duration = 10
        lunch_break_duration = 20

        # Define school hours
        start_time = 8 * 60  # 8:00 AM
        end_time = 14 * 60  # 2:00 PM

        return Schedule(grade, days_of_week, start_time, end_time, class_duration, break_duration, lunch_break_duration)