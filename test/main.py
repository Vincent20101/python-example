# coding: utf-8

def test(name):
    return int(name)


def test2():
    try:
        # return "abc"
        # test('abc')
        1 / 0
    except Exception as e:
        print(e)
        return "exception"
    finally:
        print('finally')
        # return "finally"


class Student(object):
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    @classmethod
    def get_name(cls):
        print("get_name")
        # return cls.name

    def get_age(self):
        self.get_name()
        return self.__age

    def __getattr__(self, key):
        # print("get_attribute is {}".format(self.name))
        print("get_attribute is {}".format(key))
        if self.__name:
            key = '{}.{}'.format(self.__name, key)
        else:
            key = key
        print(key)
        return Student(key)

    def __setattr__(self, key, value):
        print("set_attribute key is {}, value is {}".format(key, value))
        self.__dict__[key] = value

    def __call__(self, *args, **kwargs):
        print("args={}".format(args))
        print("kwargs={}".format(kwargs))


if __name__ == '__main__':
    print(test2())

    # Student.get_name()
    s = Student(name="xiao", age=18)
    print(s.get_age())
    s.__weight = 120
    print(Student(name="xiao", age=18).__weight)
    print("=======")
    s.a.b.c()

    str = "hello" + " world" + str(3)
    print(str)

    n = None
    if not n:
        print("not n")
    else:
        print(n)
