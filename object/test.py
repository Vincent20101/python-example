# coding:utf-8

"""
  学生信息库
"""


class StudentInfo(object):
    def __init__(self, s):
        self.students = s

    def get_by_id(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        for id_, value in self.students.items():
            print('学号：{}, 姓名:{}, 年龄:{}, 性别:{}, 班级:{}'.format(
                id_, value['name'], value['age'], value['sex'], value['class_number']
            ))
        return self.students

    def add(self, **student):
        check = self.check_user_info(**student)
        if not check:
            print(check)
            return
        self.__add(**student)

    def adds(self, new_students):
        for student in new_students:
            check = self.check_user_info(**student)
            if not check:
                print(check, student.get('name'))
                continue
            self.__add(**student)

    def __add(self, **student):
        new_id = max(self.students) + 1
        self.students[new_id] = student

    def delete(self, student_id):
        if student_id not in self.students:
            print('{} 并不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('学号是{}, {}同学的信息已经被删除了'.format(student_id, user_info['name']))

    def deletes(self, ids):
        for id_ in ids:
            if id_ not in self.students:
                print(f'{id_} 不存在学生库中')
                continue
            s_info = self.students.pop(id_)
            print(f'学号{id_} 学生{s_info["name"]} 已被移除')

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print('并不存在这个学号:{}'.format(student_id))

        check = self.check_user_info(**kwargs)
        if not check:
            print(check)
            return

        self.students[student_id] = kwargs
        print('同学信息更新完毕')

    def updates(self, update_students):
        for student in update_students:
            id_ = list(student.keys())[0]
            if id_ not in self.students:
                print(f'学号{id_} 不存在')
                continue
            user_info = student[id_]
            check = self.check_user_info(**user_info)
            if not check:
                print(check)
                continue
            self.students[id_] = user_info
        print('所有用户信息更新完成')

    def search_users(self, **kwargs):
        values = list(self.students.values())
        rs = []

        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs['sex']
        elif 'class_number' in kwargs:
            key = 'class_number'
            value = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        else:
            print('没有发现搜索的关键字')
            return

        for u in values:  # [{name, sex, age, class_number}, {}]
            if value in user[key]:
                rs.append(u)
        return rs

    @staticmethod
    def check_user_info(**kwargs):
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '缺少学生年龄'
        if 'sex' not in kwargs:
            return '缺少学生性别'
        if 'class_number' not in kwargs:
            return '缺少学生班级'
        return True


students = {
    1: {
        'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'
    },
    2: {
        'name': '小慕',
        'age': 10,
        'class_number': 'B',
        'sex': 'boy'
    },
    3: {
        'name': '小曼',
        'age': 18,
        'class_number': 'A',
        'sex': 'girl'
    },
    4: {
        'name': '小高',
        'age': 18,
        'class_number': 'C',
        'sex': 'boy'
    },
    5: {
        'name': '小云',
        'age': 18,
        'class_number': 'B',
        'sex': 'girl'
    }
}

if __name__ == '__main__':
    student_info = StudentInfo(students)
    user = student_info.get_by_id(1)
    student_info.add(name='dewei', age=34, class_number='A', sex='boy')
    users = [
        {'name': 'xiaoMing', 'age': 17, 'class_number': 'B', 'sex': 'boy'},
        {'name': 'xiaoMing', 'age': 18, 'class_number': 'C', 'sex': 'girl'}
    ]
    student_info.adds(users)
    student_info.get_all_students()
    print('------')
    student_info.deletes([7, 8])
    student_info.get_all_students()
    print('-------')
    student_info.updates([
        {1: {'name': 'dewei.zhang', 'age': 18, 'class_number': 'A', 'sex': 'boy'}},
        {2: {'name': '小慕同学', 'age': 18, 'class_number': 'A', 'sex': 'boy'}}
    ])
    student_info.get_all_students()
    result = student_info.search_users(name='d')
    print(result)
    result = student_info.search_users(name='小')
    print(result)
    print('------')
    result = student_info.search_users(name='')
    print(result)
    result = student_info.search_users(name='小')
    print(result)
    print('-----')
    result = student_info.search_users(name='')
    print(result)
