class GradeBook:
    """ЗАДАЧА: Найти имя студента с самым высоким средним баллом"""
    def __init__(self): self.students = {} # {"Ivan": [5, 4], "Oleg": [3]}
    def get_best_student(self):
        person=''
        score=0
        if len(self.students)==0:
            return None
        for student in self.students:
            if sum(self.students[student])/len(self.students[student])>score:
                score=sum(self.students[student])/len(self.students[student])
                person=student
        return person