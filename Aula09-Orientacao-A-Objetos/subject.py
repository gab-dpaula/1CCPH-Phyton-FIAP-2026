class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def show_info(self):
        print(f"Subject: {self.name} | Teacher: {self.teacher}")

# TEMPORÁRIO
# python = Subject("PCP", "Russi")
# python.show_info()
# print(python.teacher)