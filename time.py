lass Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        h = self.__hour + other.__hour
        m = self.__minute + other.__minute
        s = self.__second + other.__second

        # adjust time
        if s >= 60:
            m += s // 60
            s = s % 60
        if m >= 60:
            h += m // 60
            m = m % 60

        return Time(h, m, s)

    def show(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)


# user input
h1 = int(input("Enter hour for Time 1: "))
m1 = int(input("Enter minute for Time 1: "))
s1 = int(input("Enter second for Time 1: "))

h2 = int(input("Enter hour for Time 2: "))
m2 = int(input("Enter minute for Time 2: "))
s2 = int(input("Enter second for Time 2: "))

t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)
                                                                                                                                    

t3 = t1 + t2

print("Sum of two times:")
t3.show()


