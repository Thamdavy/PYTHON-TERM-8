class Student:
    def __init__(self, name1, student_id1):
        self.name = name1
        self.student_id = student_id1
        self.marks = []  # List datatype as Blank, no marks yet

    def student_info(self):
        print(f"Student's Name: {self.name}, ID: {self.student_id}, Scores: {self.marks}")

    def receive_mark(self, mymark):
        self.marks.append(mymark)
        print(f"Student's Name: {self.name} received score {mymark} successfully.")

    def avg_mark(self):
        if not self.marks:
            return 0
        else:
            avg = sum(self.marks) / len(self.marks)
            return avg


# Example usage
myClassmate1 = Student("Thamdavy", "S001122")
myClassmate1.student_info()

myClassmate1.receive_mark(60)
myClassmate1.student_info()

myClassmate1.receive_mark(80)
myClassmate1.student_info()

print(f"Student's Name: {myClassmate1.name}, Average Score: {myClassmate1.avg_mark()}")
