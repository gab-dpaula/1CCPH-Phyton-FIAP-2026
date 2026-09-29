from subject import Subject

class Student:
    def __init__(self, name, rm, course):
        self.name = name
        self.rm = rm
        self.course = course
        self.subjects = []
        self.score_by_subject = {}

    def registrate(self, subject: Subject):
        self.subjects.append(subject)
        self.score_by_subject.setdefault(subject.name, [])


    def add_score(self, subject: Subject, score: float):
        self.score_by_subject[subject.name].append(score)

    def calc_average_s(self, s: Subject) -> float:
        scores = self.score_by_subject.get(s.name, [])
        if not scores:
            return 0
        return sum(scores) / len(scores)

    def calc_average_score(self,) -> float:
        average_scores = []
        for s in self.subjects:
            average_scores_s = self.calc_average_s(s)
            average_scores.append(average_scores_s)

        return sum(average_scores) / len(average_scores)
