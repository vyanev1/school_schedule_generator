# Class Scheduling Project

## Overview

This project provides a simple scheduling system for high school classes. It includes functionality to schedule classes and print the resulting schedules.

## Files

- `constants`: The directory contains defined constants in the program
- `model`: The directory contains classes for `Grade`, `Subject`, `Teacher`, `Schedule`, and `TimeSlot`.
- `main.py`: Main script containing class scheduling logic and schedule printing.
- `README.md`: Documentation file (you are here).

## How to Use

1. Run `main.py` to schedule classes for predefined grades (eighth and ninth).
2. The schedules will be printed, showing the allocated subjects, teachers, and time slots.

## Classes

### `Grade`

Represents a school grade with associated subjects and their details.

### `Subject`

Represents a school subject with associated teachers and scheduling constraints.

### `Teacher`
Represents a school teacher, contains information about the teacher's name and occupied time slots

### `TimeSlot`
Represents a time slot in the schedule, contains information about the start time, end time, subject and teacher name

### `Schedule`

Handles the scheduling of classes for a specific grade, considering time slots and teacher availability.

## Sample Usage

```python
# Define grades with subjects and create schedules
eighth_grade = Grade(8, subjects=[...])
eighth_grade_schedule = Schedule(eighth_grade)

ninth_grade = Grade(9, subjects=[...])
ninth_grade_schedule = Schedule(ninth_grade)

# Schedule classes for grades
grade_schedules = [eighth_grade_schedule, ninth_grade_schedule]
schedule_classes(grade_schedules)

# Print the resulting schedules
for s in grade_schedules:
    s.print_schedule()
```

## Contributors

- Victor Yanev
