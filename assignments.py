class Week2:
    a = 0
    b = 0

    def a1(self):
        self.a = int(input())
        print(self.a)

    def a2(self):
        self.a, self.b = input().split(" ")
        self.a = int(self.a)
        self.b = int(self.b)
        print(self.a * self.b)

    def a3(self):
        self.a, self.b = input().split(" ")
        self.a = int(self.a)
        self.b = int(self.b)
        if self.a > self.b:
            print(self.a)
        else:
            print(self.b)


class Week3:
    a = 0
    b = 0
    n = 0

    def a1(self):
        self.a = [int(i) for i in input().split()]
        for i in self.a:
            if abs(i) % 10 != 4:
                print(i, end=" ")

    def a2(self):
        self.a = [int(i) for i in input().split()]
        self.b = []
        for i in self.a:
            if i not in self.b:
                self.a.append(i)
        self.b.sort()
        if (len(self.b) == 1):
            print(2 * self.b[0])
        else:
            print(self.b[1] + self.b[-2])

    def a3(self):
        self.n = int(input())
        self.a = [int(i) for i in input().split()]
        self.b = []
        for i in self.a:
            if i not in self.b:
                self.b.append(i)
                print(i, end=" ")


class Week4:
    a = 0
    b = 0

    def hcf(self, a, b):
        if b == 0:
            return a
        else:
            return self.hcf(b, a % b)

    def factorial(self, n):
        if n == 1:
            return n
        elif n < 1:
            return "NA"
        else:
            return n * self.factorial(n - 1)

    def a1(self):
        self.a = int(input())
        self.b = int(input())
        print(self.hcf(self.a, self.b))

    # This code passes sample cases 3/4 and test cases 2/3 for assignment 2. If a+b is checked with >=20 it passes
    # 4/4 sample cases but only 1/3 test cases. So, if anyone can find the issue here, please suggest!
    def a2(self):
        self.a = int(input())
        self.b = int(input())
        if self.a + self.b > 20:
            print('invalid')
        else:
            print(int(self.factorial(self.a) * self.factorial(self.a + 1) / self.factorial(self.a + 1 - self.b)))

    def a3(self):
        self.a = int(input())
        self.b = 1
        for i in range(self.a):
            for j in range(i + 1):
                print(self.b * self.b, end=" ")
                self.b += 1
            print()
