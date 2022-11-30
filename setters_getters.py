class Student:

    def __init__(self, name):
        self.__name = name
        self.age = 18

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name.isalpha():
            self.__name = new_name
        else:
            raise Exception('В имени не должно быть цифр')


    @name.deleter
    def name(self):
        raise Exception('Удалять нельзя')


    # name = property(get_name, set_name, delete_name)


s = Student(name='Iman')
print(s.name)
s.name = 'Myrza'
print(s.name)
print(s.age)
del s.age

