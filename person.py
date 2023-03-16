from address import Address

class Person:
    def __init__(self, first, last, dob, phone, address):
        self.__first_name = first
        self.__last_name = last
        self.__date_of_birth = dob
        self.__phone = phone
        self.__addresses = []
        
        if isinstance(addess, Address):
            self.__addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise Error("Invalid Address...")
            self.__addresses = address
        else:
            raise Error("Invalid Address...")
    
    def add_address(self, address):
        if not isinstance(address, Address):
            raise Error("Invalid Address...")
        self.__addresses.append(address)

        