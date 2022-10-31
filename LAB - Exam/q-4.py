class student:
    
    school = "ABC"
    
    @classmethod       
    def get_school(cls):
        return cls.school
    
print(student.get_school())