from .karmaCommand import KarmaCommand
from .karmaLog import KarmaLog

class IncreaseKarma(KarmaCommand):
    def __init__(self, student, points):
        super().__init__(student)
        self.points = points

    def execute(self):
        self.student.karma += self.points
        self.student.save()
        KarmaLog(student_id=self.student.ID, change=self.points, action='increase').save()