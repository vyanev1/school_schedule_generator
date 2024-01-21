class TimeSlot:
    def __init__(self, day: str, start: int, end: int, subject_name: str = None, teacher_name: str = None):
        self.day = day
        self.start = start
        self.end = end
        self.subject_name = subject_name
        self.teacher_name = teacher_name

    def occupy(self, grade_number: int, subject_name: str, teacher_name: str):
        self.grade_number = grade_number
        self.subject_name = subject_name
        self.teacher_name = teacher_name

    def is_empty(self):
        return self.subject_name is None

    def mark_as_empty(self):
        self.subject_name = None
        self.teacher_name = None
