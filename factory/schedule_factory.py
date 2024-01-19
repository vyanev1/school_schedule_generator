from model.grade import Grade
from model.schedule import Schedule


class ScheduleFactory:

    @staticmethod
    def create_schedule(grade: Grade) -> Schedule:
        # Define class duration, break duration, and lunch break duration in minutes
        class_duration = 60
        break_duration = 10
        lunch_break_duration = 20

        # Define school hours
        start_time = 8 * 60  # 8:00 AM
        end_time = 14 * 60  # 2:00 PM

        return Schedule(grade, start_time, end_time, class_duration, break_duration, lunch_break_duration)