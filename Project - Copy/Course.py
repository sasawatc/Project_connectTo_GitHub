__author__ = 'win.thitiwat'


class Course():
    def __init__(self, title, courseID, courseTimeTable, lecturer, description, credit):
        self.course_title = title
        self.course_id = courseID
        self.course_timetable = courseTimeTable
        self.course_lecturer = lecturer
        self.course_description = description
        self.course_credit = credit


