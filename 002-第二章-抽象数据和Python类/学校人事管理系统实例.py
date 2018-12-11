import datetime


class PersonValueError(ValueError):
    pass


class PersonTypeError(TypeError):
    pass


class Person:
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str)) and sex in ('女', '男'):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)  # 生成一个日期对象:datetime.date(*(2018, 1, 3))
        except Exception as e:
            str(e)
            raise PersonValueError('Wrong date:', birthday)

        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return datetime.date.today().year - self._birthday.year

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonTypeError('set_name', name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id

    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return '  '.join((self._id, self._name, self._sex, str(self._birthday)))

    def details(self):
        return ', '.join(
            (
                '编号: ' + self._id,
                '姓名: ' + self._name,
                '性别: ' + self._sex,
                '出生日期: ' + str(self._birthday)
            )
        )


class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):  # 实现学生号生成规则
        cls._id_num += 1
        year = datetime.date.today().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        # 三种初始化父类方法
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        # super(Student, self).__init__(name, sex, birthday, Student._id_gen())  # python2
        # super().__init__(name, sex, birthday, Student._id_gen())  # python3
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}  # 一个空字典

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError('No this course selected:', course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    def details(self):
        return ', '.join(
            (
                Person.details(self),
                '入学日期: ' + str(self._enroll_date),
                '院系: ' + self._department,
                '课程记录: ' + str(self.scores())
            )
        )


class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return '0{:04}{:05}'.format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except Exception as e:
                str(e)
                raise PersonValueError('Wrong date: ', entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1720
        self._department = '未定'
        self._position = '未定'

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self, position):
        self._position = position

    def set_department(self, department):
        self._department = department

    def details(self):
        return ', '.join(
            (
                super().details(),
                '入职日期: ' + str(self._entry_date),
                '院系: ' + self._department,
                '职位: ' + self._position,
                '工资: ' + str(self._salary)
            )
        )


'''
p1 = Person('谢雨洁', '女', (1995, 7, 30), '1201510111')
p2 = Person('汪力强', '男', (1990, 2, 17), '1201380324')
p3 = Person('张子玉', '女', (1974, 10, 16), '0197401032')
p4 = Student('李国栋', '男', (2008, 5, 24), '0196212018')
plist2 = [p1, p2, p3, p4]
for p in plist2:
    print(p)

print('\nAnother sorting:')
plist2.sort()
# plist2.sort(reverse=True)
for p in plist2:
    print(p.details())
'''
p1 = Staff('张子玉', '女', (1974, 10, 16))
p2 = Staff('李国栋', '男', (2008, 5, 24))
print(p1)
print(p2)
p1.set_department('数学')
p1.set_position('副教授')
p1.set_salary(8400)
print(p1.details())
print(p2.details())
