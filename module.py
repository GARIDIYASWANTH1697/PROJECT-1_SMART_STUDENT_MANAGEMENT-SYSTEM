class Student:
    def __init__(self, student_id, student_name, age, course, subjects):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = age
        self.student_course = course
        self.subjects = subjects


    def to_dict(self):

        return {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "student_age": self.student_age,
            "student_course": self.student_course,
            "subjects": self.subjects
        }
            
      
