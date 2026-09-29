from student import Student
from subject import Subject

# CRIAR / INSTANCIAR 1 Aluno
student1 = Student("Gabriel", "573195", "Computer Science")

#CRIAR / INSTANCIAR 2 Disciplines
prompt_ia = Subject("Prompt IA", "Jorge")
sers = Subject("Renewable Solutions", "André")

# MATRICULAR O ALUNO NAS DISCIPLINAS
student1.registrate(prompt_ia)
student1.registrate(sers)

# ADICIONAR NOTA DO ALUNO REFERENTE ÀS DISCIPLINAS
student1.add_score(prompt_ia, 10)
student1.add_score(prompt_ia, 8)
student1.add_score(sers, 5)
student1.add_score(sers, 3)

