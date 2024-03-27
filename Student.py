class Student:

    def __init__(self, name, major, gpa, has_enrolled):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.has_enrolled = has_enrolled

    def on_honor_roll(self):
        if self.gpa >= 7:
            return True
        else:
            return False