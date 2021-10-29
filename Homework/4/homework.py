class LongInt:
    MINUS = 0
    PLUS = 1

    def __init__(self, number, sign=PLUS):
        if type(number) == str:
            self.n = len(number)
            self.sign = sign
            self.lst = []
            self.set_int_list_by_str(number)
        elif type(number) == list:
            self.n = len(number)
            self.sign = sign
            self.lst = number
            self.check_lst()
        elif type(number) == LongInt:
            self.n = len(number.lst)
            self.lst = [i for i in number.lst]
            self.sign = number.sign

    def check_lst(self):
        k = 0
        for i in range(1, self.n + 1):
            if self.lst[-i] == 0:
                k += 1
            else:
                break
        if k != 0:
            self.lst = self.lst[:-k]
            self.n -= k

    def set_int_list_by_str(self, string):
        if string[0] == '-':
            self.sign = self.MINUS

        for i in range(1, self.n + self.sign):
            self.lst.append(int(string[-i]))

    @staticmethod
    def add_positive(a, b):
        a = LongInt(a)
        b = LongInt(b)
        if a.n != b.n:
            if a.n > b.n:
                b.lst += [0 * (a.n - b.n)]
                b.n = a.n
            else:
                a.lst += [0 * (b.n - a.n)]
                a.n = b.n

        lst = []
        temp = 0

        for i in range(a.n):
            lst.append((a.lst[i] + b.lst[i] + temp) % 10)
            temp = (a.lst[i] + b.lst[i] + temp) // 10

        if temp != 0:
            lst.append(temp)

        return LongInt(lst)

    @staticmethod
    def subtract_positive(a, b):
        a = LongInt(a)
        b = LongInt(b)

        a.set_sign(LongInt.PLUS)
        b.set_sign(LongInt.PLUS)

        if a == b:
            return LongInt('0')
        else:
            if a > b:
                if a.n > b.n:
                    b.lst += [0 * (a.n - b.n)]
                    b.n = a.n

                for i in range(a.n):
                    a.lst[i] -= b.lst[i]
                    if a.lst[i] < 0:
                        a.lst[i] += 10
                        a.lst[i + 1] -= 1

                return LongInt(a.lst)
            else:
                new_number = LongInt.subtract_positive(b, a)
                new_number.switch_sign()
                return new_number

    def set_sign(self, sign):
        self.sign = sign

    def switch_sign(self):
        if self.sign == self.MINUS:
            self.sign = self.PLUS
        else:
            self.sign = self.MINUS

    def __add__(self, other):
        if self.sign == other.sign:
            new_number = self.add_positive(self, other)
            new_number.set_sign(self.sign)

            return new_number
        else:
            if self.sign == self.PLUS:
                return self.subtract_positive(self, other)
            else:
                return self.subtract_positive(other, self)

    def __eq__(self, other):
        return self.sign == other.sign and self.lst == other.lst

    def __ne__(self, other):
        return self.sign != other.sign or self.lst != other.lst

    def __lt__(self, other):
        if self == other:
            return False

        if self.sign == other.sign:
            if self.n == other.n:
                for i in range(1, self.n + 1):
                    if other.lst[-i] > self.lst[-i]:
                        return self.sign == self.PLUS
                    elif other.lst[-i] < self.lst[-i]:
                        return self.sign == self.MINUS
            else:
                if self.sign == self.PLUS:
                    return self.n < other.n
                else:
                    return not (self.n < other.n)
        else:
            return self.sign < other.sign

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def __str__(self):
        string = f'{"-" if self.sign == self.MINUS else ""}'

        for i in range(1, self.n + 1):
            string += str(self.lst[-i])

        return "LongInt: " + string


tests = [
    not bool(LongInt('100') < LongInt('100')),
    not bool(LongInt('101') < LongInt('100')),
    not bool(LongInt('100') < LongInt('99')),
    not bool(LongInt('100') < LongInt('-100')),
    not bool(LongInt('101') < LongInt('-100')),
    not bool(LongInt('100') < LongInt('-99')),
    bool(LongInt('100') < LongInt('101')),
    bool(LongInt('99') < LongInt('101')),
    bool(LongInt('-100') < LongInt('99')),
    bool(LongInt('-102') < LongInt('-100')),
    bool(LongInt('-100') < LongInt('-99')),
    not bool(LongInt('100') > LongInt('100')),
    bool(LongInt('101') > LongInt('100')),
    bool(LongInt('100') > LongInt('99')),
    bool(LongInt('100') > LongInt('-100')),
    bool(LongInt('101') > LongInt('-100')),
    bool(LongInt('100') > LongInt('-99')),
    not bool(LongInt('100') > LongInt('101')),
    not bool(LongInt('99') > LongInt('101')),
    not bool(LongInt('-100') > LongInt('99')),
    not bool(LongInt('-102') > LongInt('-100')),
    not bool(LongInt('-100') > LongInt('-99')),
    bool(LongInt('100') <= LongInt('100')),
    not bool(LongInt('101') <= LongInt('100')),
    not bool(LongInt('100') <= LongInt('99')),
    not bool(LongInt('100') <= LongInt('-100')),
    not bool(LongInt('101') <= LongInt('-100')),
    not bool(LongInt('100') <= LongInt('-99')),
    bool(LongInt('100') <= LongInt('101')),
    bool(LongInt('99') <= LongInt('101')),
    bool(LongInt('-100') <= LongInt('99')),
    bool(LongInt('-102') <= LongInt('-100')),
    bool(LongInt('-100') <= LongInt('-99')),
    bool(LongInt('100') >= LongInt('100')),
    bool(LongInt('101') >= LongInt('100')),
    bool(LongInt('100') >= LongInt('99')),
    bool(LongInt('100') >= LongInt('-100')),
    bool(LongInt('101') >= LongInt('-100')),
    bool(LongInt('100') >= LongInt('-99')),
    not bool(LongInt('100') >= LongInt('101')),
    not bool(LongInt('99') >= LongInt('101')),
    not bool(LongInt('-100') >= LongInt('99')),
    not bool(LongInt('-102') >= LongInt('-100')),
    not bool(LongInt('-100') >= LongInt('-99')),
    LongInt('100') + LongInt('100') == LongInt('200'),
    LongInt('-100') + LongInt('100') == LongInt('0'),
    LongInt('-100') + LongInt('-100') == LongInt('-200'),
    LongInt('100') + LongInt('99') == LongInt('199'),
    LongInt('99') + LongInt('99') == LongInt('198'),
    LongInt('-99') + LongInt('100') == LongInt('1'),
    LongInt('99') + LongInt('-100') == LongInt('-1'),
    LongInt('101') + LongInt('-100') == LongInt('1'),

]

print(f"Pass: {tests.count(True)} Fail: {tests.count(False)}")
