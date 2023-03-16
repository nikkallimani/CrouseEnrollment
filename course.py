from professor import Professor
from enroll import Enroll

class Course:
    
    def __init__(self, name, code, max_, min_, professor):
        self.__name = name
        self.__code = code
        self.__max = max_
        self.__min = min_
        self.__professors = []
        self.__enrollments = []
    
        if isinstance(professor, Professor):
            self.__professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Error("Invalid professor...")
            
            self.professors.append(professor)
        else:
            raise Error("Invalid professor...")
        
    def add_professor(self,professor):
        if not isinstance(professor, Professor):
            raise Error("Invalid Professor")
        
        self.__professors.append(professor)
    
    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Error("Invalid Enroll...")
        
        if len(self.__enrollments) == self.__max:
            raise Error(Cann't enroll, course is full")
            
        self.enrollments.append(enroll)
    
    def is_cancelled(self):
        return len(self.__enrollments) < self.__min