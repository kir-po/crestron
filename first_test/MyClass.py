class Person:
    '''
        С self работает так:
        myoject.method(arg1, arg2) == MyClass.method(myobject, arg1, arg2)
    '''

    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Привет! Как дела? Меня зовут', self.name)


class Men(Person):  ###Класс Men - наследник Person
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age

    def whoIAm(self):
        print('Я мужииииик! И меня зовут {0}'.format(self.name))


p = Person('Кирилл')
p.sayHi()
m = Men('Васян', 41)
m.whoIAm()
