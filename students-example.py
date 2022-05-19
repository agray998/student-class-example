class Student():
    students = []
    def __init__(self, name, age, class_ = "student"):
        self.name = name
        self.age = age
        self.class_ = class_
        Student.students.append(self)

    def search(search_term, search_by = None):
        if search_by:
            results = map(str, filter(lambda s: getattr(s, search_by) == search_term, Student.students))
            # results = []
            # for student in Student.students:
            #     if getattr(student, search_by) == search_term:
            #         results.append(str(student))
        else:
            results = map(str, Student.students)
        return results

    def avg_mark(self, *scores):
        avg = sum(scores) // len(scores)
        self.avg = avg
        print(self.name, "attained an average score of", str(avg) + '%')
    
    def __str__(self):
        return f"Student name: {self.name}, student age: {self.age}, class: {self.class_}"

def main():
    while True:
        mode = input("[A]dd or [S]earch? ").upper()
        if mode == 'A':
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            class_ = input("Enter class: ")
            student = Student(name, age, class_) if class_ else Student(name, age)
            print(student)
            scores = input("Enter test scores: ")
            scores_list = map(int, scores.replace(" ", "").split(','))
            student.avg_mark(*scores_list)
        elif mode == 'S':
            search_by = input("Attribute to search by: ")
            search_term = input("Value to match: ")
            print('\n'.join(Student.search(search_term, search_by)))
        if input("Continue? (Y/N): ").upper() == 'N':
            break

if __name__ == '__main__':
    main()