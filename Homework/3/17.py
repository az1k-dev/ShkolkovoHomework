class Person:
    def __init__(self, surname: str, name: str, patronymic: str, age: int):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic

    def is_adult(self):
        return self.age >= 18

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic} {self.age}"


def main():
    n = int(input())

    lst = []

    for i in range(n):
        surname, name, palytronomic, age = input().split()
        age = int(age)
        person = Person(surname, name, palytronomic, age)
        lst.append(person)

    heap_sort(lst)

    for i in lst:
        print(i)


def heapify(a, i=0, finish=None, start=False):
    if finish is None:
        finish = len(a)

    i1 = i * 2 + 1
    i2 = i * 2 + 2

    if not i1 < finish:
        return

    if not i2 < finish:
        if a[i1] > a[i]:
            a[i], a[i1] = a[i1], a[i]
        return

    if start:
        heapify(a, i1, finish, start)
        heapify(a, i2, finish, start)

    if a[i1] > a[i] or a[i2] > a[i]:
        if a[i1] > a[i2]:
            a[i1], a[i] = a[i], a[i1]
            heapify(a, i1, finish)
        else:
            a[i2], a[i] = a[i], a[i2]
            heapify(a, i2, finish)


def heap_sort(a):
    n = len(a)

    heapify(a, start=True)

    for i in range(n):
        j = n - i

        heapify(a, finish=j)

        a[0], a[j - 1] = a[j - 1], a[0]


if __name__ == '__main__':
    main()
