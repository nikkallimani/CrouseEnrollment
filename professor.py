from person import Person

class Professor(Person):

    def __init__(self, first, last, dob, phone, address, salary):
        super().__init__(self, first, last, dob, phone, address)
        self.__salary = salary
        self.__courses = []
        self.__got_raise = False
        
    def check_for_raise(self):
        if len(self.courses)>4 and not self.__got_raise:
            self.__salary += 20000
            self.__got_raise = Ture
    
    def add_course(self, course):
        if not isinstance(course, Course):
            raise Error("Invalid Course...")
        self.__courses.append(course)
    
        